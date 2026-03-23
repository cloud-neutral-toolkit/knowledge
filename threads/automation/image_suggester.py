#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "automation" / "build"
QUEUE_JSON = BUILD_DIR / "publish-queue.json"
OUT_JSON = BUILD_DIR / "image-suggestions.json"

BUILD_DIR.mkdir(parents=True, exist_ok=True)


def load_queue():
    if not QUEUE_JSON.exists():
        raise SystemExit("publish-queue.json not found. Run x_publish.py build-queue first.")
    return json.loads(QUEUE_JSON.read_text(encoding="utf-8"))


def infer_brief(entry: dict) -> dict:
    kind = entry["kind"]
    topic = entry["topic"]
    asset_type = entry.get("asset_type", "card")

    palette = "dark neutral / cloud infra / blueprint accents"
    if asset_type == "quote-card":
        return {
            "asset_type": asset_type,
            "title": topic,
            "visual_style": "minimal quote card",
            "palette": palette,
            "layout": "large statement + tiny attribution/footer",
            "must_include": [topic, "@Cloud_Neutral"],
            "notebooklm_prompt": f"从相关文章中提炼支撑观点『{topic}』的 3 个关键词和 1 句最适合上卡片的短句。",
        }
    if asset_type == "diagram":
        return {
            "asset_type": asset_type,
            "title": topic,
            "visual_style": "clean architecture diagram",
            "palette": palette,
            "layout": "3-step or layered system diagram",
            "must_include": [topic, "trade-offs", "stage / boundary / flow"],
            "notebooklm_prompt": f"从相关文章中提炼主题『{topic}』的阶段、系统组件、流向与关键 trade-off，输出成图解提纲。",
        }
    if asset_type == "screenshot":
        return {
            "asset_type": asset_type,
            "title": topic,
            "visual_style": "annotated product/article screenshot",
            "palette": palette,
            "layout": "screenshot + callouts",
            "must_include": [topic, "1-2 highlights"],
            "notebooklm_prompt": f"从相关文章中提炼主题『{topic}』最值得标注的 3 个要点，适合覆盖在截图上。",
        }
    return {
        "asset_type": asset_type,
        "title": topic,
        "visual_style": "tool radar card",
        "palette": palette,
        "layout": "tool name + layer + verdict + trade-off",
        "must_include": [topic, entry.get("goal", "awareness")],
        "notebooklm_prompt": f"从相关文章中提炼主题『{topic}』最值得做成 Radar 卡片的 1 句 verdict、3 个能力点、2 个 trade-off。",
    }


def main():
    parser = argparse.ArgumentParser(description="Generate image suggestions for X queue")
    parser.add_argument("suggest", nargs="?", default="suggest")
    args = parser.parse_args()
    queue = load_queue()
    suggestions = []
    for entry in queue:
        suggestions.append(
            {
                "date": entry["date"],
                "topic": entry["topic"],
                "kind": entry["kind"],
                "source_file": entry["source_file"],
                "suggestion": infer_brief(entry),
            }
        )
    OUT_JSON.write_text(json.dumps(suggestions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(suggestions, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
