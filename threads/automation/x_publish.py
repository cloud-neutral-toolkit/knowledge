#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_DIR = ROOT / "automation"
BUILD_DIR = AUTOMATION_DIR / "build"
STATE_DIR = AUTOMATION_DIR / "state"
QUEUE_MD = ROOT / "x-publish-queue.md"
QUEUE_JSON = BUILD_DIR / "publish-queue.json"
STATE_JSON = STATE_DIR / "publish-state.json"

BUILD_DIR.mkdir(parents=True, exist_ok=True)
STATE_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_TIMES = {
    "周一": "09:00",
    "周三": "21:00",
    "周五": "09:00",
    "周日": "21:00",
}


@dataclass
class Item:
    index: int
    kind: str
    text: str


@dataclass
class QueueEntry:
    date: str
    weekday: str
    kind: str
    topic: str
    source_file: str
    preferred_time: str
    goal: str
    cta: str
    asset_type: str
    status: str
    items: List[Item]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_state() -> dict:
    if STATE_JSON.exists():
        return json.loads(STATE_JSON.read_text(encoding="utf-8"))
    return {"published": {}}


def infer_goal(kind: str) -> str:
    return {
        "radar": "establish-positioning",
        "thread": "growth",
        "opinion": "worldview",
        "longform": "traffic",
    }.get(kind, "awareness")


def infer_cta(kind: str) -> str:
    return {
        "radar": "bookmark / follow",
        "thread": "RT / follow",
        "opinion": "reply / discuss",
        "longform": "read / click-through",
    }.get(kind, "engage")


def infer_asset_type(kind: str, topic: str) -> str:
    t = topic.lower()
    if kind == "thread":
        return "diagram"
    if kind == "radar":
        return "card"
    if kind == "opinion":
        return "quote-card"
    if any(x in t for x in ["migration", "architecture", "k8s", "database", "边界"]):
        return "diagram"
    return "card"


def classify_kind(raw_type: str) -> str:
    raw = raw_type.lower()
    if "thread" in raw:
        return "thread"
    if "radar" in raw:
        return "radar"
    if "观点" in raw:
        return "opinion"
    if "导流" in raw or "长文" in raw:
        return "longform"
    return "post"


def extract_code_blocks(md: str) -> List[str]:
    return [m.strip() for m in re.findall(r"```\n(.*?)```", md, flags=re.S)]


def parse_week_file(path: Path) -> List[List[Item]]:
    text = load_text(path)
    sections = re.split(r"(?=^##\s+📅\s+\d{2}-\d{2})", text, flags=re.M)
    groups: List[List[Item]] = []

    for section in sections:
        if not re.search(r"^##\s+📅\s+\d{2}-\d{2}", section, flags=re.M):
            continue
        blocks = extract_code_blocks(section)
        if not blocks:
            continue

        first_lines = [b.splitlines()[0].strip() if b.splitlines() else "" for b in blocks]
        is_thread = len(blocks) > 1 and all(re.match(r"\d+/\d+", line) for line in first_lines)
        if is_thread:
            items = []
            for i, block in enumerate(blocks, start=1):
                items.append(Item(index=i, kind="post" if i == 1 else "reply", text=block))
            groups.append(items)
        else:
            groups.append([Item(index=1, kind="post", text=blocks[0])])

    return groups


def parse_queue_md() -> List[dict]:
    text = load_text(QUEUE_MD)
    pattern = re.compile(
        r"\|\s*(\d{2}-\d{2})\s*\|\s*(周.?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([⬜✅🔄❌].*?)\s*\|"
    )
    rows = []
    current_week_file = None
    current_year = None
    for line in text.splitlines():
        week_match = re.search(r"第\s*(\d+)\s*周.*?(\d{4})-(\d{2})-(\d{2}).*?~", line)
        if week_match:
            week_num = int(week_match.group(1))
            current_week_file = f"week-{week_num:02d}.md"
            current_year = week_match.group(2)
        m = pattern.search(line)
        if m and current_week_file and current_year:
            mmdd, weekday, raw_type, topic, status = m.groups()
            rows.append(
                {
                    "date": f"{current_year}-{mmdd}",
                    "weekday": weekday,
                    "raw_type": raw_type.strip(),
                    "kind": classify_kind(raw_type.strip()),
                    "topic": topic.strip(),
                    "status": status.strip(),
                    "source_file": current_week_file,
                }
            )
    return rows


def build_queue() -> List[QueueEntry]:
    rows = parse_queue_md()
    week_cache: dict[str, List[List[Item]]] = {}
    result: List[QueueEntry] = []
    per_file_cursor: dict[str, int] = {}

    for row in rows:
        source = ROOT / row["source_file"]
        if row["source_file"] not in week_cache:
            week_cache[row["source_file"]] = parse_week_file(source)
            per_file_cursor[row["source_file"]] = 0

        groups = week_cache[row["source_file"]]
        cursor = per_file_cursor[row["source_file"]]
        items = groups[cursor] if cursor < len(groups) else []
        per_file_cursor[row["source_file"]] = cursor + 1

        entry = QueueEntry(
            date=row["date"],
            weekday=row["weekday"],
            kind=row["kind"],
            topic=row["topic"],
            source_file=row["source_file"],
            preferred_time=DEFAULT_TIMES.get(row["weekday"], "21:00"),
            goal=infer_goal(row["kind"]),
            cta=infer_cta(row["kind"]),
            asset_type=infer_asset_type(row["kind"], row["topic"]),
            status=row["status"],
            items=items,
        )
        result.append(entry)
    save_json(QUEUE_JSON, [serialize_entry(e) for e in result])
    return result


def serialize_entry(entry: QueueEntry) -> dict:
    data = asdict(entry)
    data["items"] = [asdict(i) for i in entry.items]
    return data


def load_queue() -> List[dict]:
    if not QUEUE_JSON.exists():
        build_queue()
    return json.loads(QUEUE_JSON.read_text(encoding="utf-8"))


def find_entry(date: str) -> Optional[dict]:
    for entry in load_queue():
        if entry["date"] == date:
            return entry
    return None


def get_today_shanghai() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")


def normalize_status_line(url: Optional[str]) -> str:
    return f"✅ {url}" if url else "✅"


def ensure_xurl_ready() -> None:
    proc = subprocess.run(["xurl", "auth", "status"], capture_output=True, text=True)
    out = (proc.stdout + proc.stderr).strip()
    if proc.returncode != 0 or "No apps registered" in out or "Unauthorized" in out:
        raise SystemExit(f"xurl not ready: {out}")


def run_xurl_post(text: str) -> str:
    proc = subprocess.run(["xurl", "post", text], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout + proc.stderr)
    return proc.stdout


def run_xurl_reply(target: str, text: str) -> str:
    proc = subprocess.run(["xurl", "reply", target, text], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout + proc.stderr)
    return proc.stdout


def extract_post_id(output: str) -> Optional[str]:
    try:
        data = json.loads(output)
        return data.get("data", {}).get("id")
    except Exception:
        m = re.search(r'"id"\s*:\s*"(\d+)"', output)
        return m.group(1) if m else None


def publish_entry(entry: dict, dry_run: bool) -> dict:
    state = load_state()
    if entry["date"] in state["published"]:
        return {"status": "already_published", "date": entry["date"], "state": state["published"][entry["date"]]}

    if dry_run:
        return {
            "status": "dry_run",
            "date": entry["date"],
            "topic": entry["topic"],
            "kind": entry["kind"],
            "items": entry["items"],
        }

    if os.environ.get("X_PUBLISH_CONFIRM") != "YES":
        raise SystemExit("Refusing real publish without X_PUBLISH_CONFIRM=YES")

    ensure_xurl_ready()

    published_ids: List[str] = []
    first_post_url = None
    for idx, item in enumerate(entry["items"], start=1):
        if idx == 1:
            output = run_xurl_post(item["text"])
        else:
            output = run_xurl_reply(published_ids[-1], item["text"])
        post_id = extract_post_id(output)
        normalized_id = post_id or f"unknown-{idx}"
        published_ids.append(normalized_id)
        if idx == 1 and post_id:
            first_post_url = f"https://x.com/i/web/status/{post_id}"

    state["published"][entry["date"]] = {
        "topic": entry["topic"],
        "kind": entry["kind"],
        "post_ids": published_ids,
        "source_file": entry["source_file"],
        "url": first_post_url,
        "published_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
    }
    save_json(STATE_JSON, state)
    return state["published"][entry["date"]]


def cmd_build_queue(_args):
    entries = build_queue()
    print(json.dumps([serialize_entry(e) for e in entries], ensure_ascii=False, indent=2))


def cmd_show(args):
    entry = find_entry(args.date)
    if not entry:
        raise SystemExit(f"No entry found for {args.date}")
    print(json.dumps(entry, ensure_ascii=False, indent=2))


def sync_status_to_md(date: Optional[str] = None) -> dict:
    state = load_state()
    published = state.get("published", {})
    text = load_text(QUEUE_MD)
    updated = text
    changed = []

    for pub_date, meta in published.items():
        if date and pub_date != date:
            continue
        mmdd = pub_date[5:]
        pattern = re.compile(
            rf"(\|\s*{re.escape(mmdd)}\s*\|\s*周.?\s*\|\s*[^|]+\|\s*[^|]+\|\s*)([⬜✅🔄❌][^|]*?)(\s*\|)",
            re.M,
        )
        replacement = rf"\1{normalize_status_line(meta.get('url'))}\3"
        new_updated, count = pattern.subn(replacement, updated, count=1)
        if count:
            updated = new_updated
            changed.append({"date": pub_date, "url": meta.get("url")})

    if updated != text:
        QUEUE_MD.write_text(updated, encoding="utf-8")
    return {"changed": changed, "count": len(changed)}


def cmd_publish(args):
    entry = find_entry(args.date)
    if not entry:
        raise SystemExit(f"No entry found for {args.date}")
    result = publish_entry(entry, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_publish_today(args):
    date = args.date or get_today_shanghai()
    entry = find_entry(date)
    if not entry:
        raise SystemExit(f"No entry found for {date}")
    result = publish_entry(entry, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_sync_status(args):
    result = sync_status_to_md(date=args.date)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Cloud_Neutral X publisher")
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build-queue")
    p_build.set_defaults(func=cmd_build_queue)

    p_show = sub.add_parser("show")
    p_show.add_argument("--date", required=True)
    p_show.set_defaults(func=cmd_show)

    p_pub = sub.add_parser("publish")
    p_pub.add_argument("--date", required=True)
    p_pub.add_argument("--dry-run", action="store_true")
    p_pub.set_defaults(func=cmd_publish)

    p_pub_today = sub.add_parser("publish-today")
    p_pub_today.add_argument("--date", required=False)
    p_pub_today.add_argument("--dry-run", action="store_true")
    p_pub_today.set_defaults(func=cmd_publish_today)

    p_sync = sub.add_parser("sync-status-to-md")
    p_sync.add_argument("--date", required=False)
    p_sync.set_defaults(func=cmd_sync_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
