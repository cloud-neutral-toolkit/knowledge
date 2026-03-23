# X 自动发布系统设计

面向 `@Cloud_Neutral` 的内容调度与发布自动化。

## 目标

这套系统解决 4 件事：

1. 把 `x-publish-queue.md` 从人读队列变成可执行队列
2. 从 `week-xx.md` 自动提取单条推文 / thread 内容
3. 支持定时 dry-run、正式发布、状态回填
4. 为每条内容生成统一的图片建议

## 目录结构

```text
knowledge/threads/
├── x-publish-queue.md              # 人类维护的总控表
├── week-01.md ... week-12.md       # 周内容源
└── automation/
    ├── README.md                   # 本文档
    ├── x_publish.py                # 主发布器 / 队列构建器
    ├── image_suggester.py          # 图片建议生成器
    ├── config.example.yaml         # 配置样例
    ├── build/
    │   ├── publish-queue.json      # 可执行发布队列（生成）
    │   └── image-suggestions.json  # 图片建议（生成）
    └── state/
        └── publish-state.json      # 发布状态（运行生成）
```

## 工作流

### 1) build-queue

从：
- `x-publish-queue.md`
- `week-xx.md`

构建出：
- `automation/build/publish-queue.json`

每个条目包含：
- 日期
- 星期
- 类型（radar / thread / opinion / longform）
- 主题
- 周文件路径
- 发布时间建议
- 内容条目列表
- CTA / 目标 / 图片类型（基于规则推断）

### 2) suggest-images

根据内容类型与主题生成图片建议：
- `card`
- `diagram`
- `quote-card`
- `screenshot`
- `none`

输出到：
- `automation/build/image-suggestions.json`

### 3) publish

支持两种模式：

- `--dry-run`：只打印将要发什么
- 正式发布：调用 `xurl post` / `xurl reply`

发布 thread 时：
1. 先发主帖
2. 逐条 reply 到上一条
3. 记录返回的 post id
4. 更新 `publish-state.json`

### 4) publish-today

根据 `Asia/Shanghai` 当前日期自动找到当天条目。

适合 cron：

```bash
python automation/x_publish.py publish-today --dry-run
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish-today
```

### 5) sync-status-to-md

把 `state/publish-state.json` 中已发布条目的状态回填到 `x-publish-queue.md`：
- `⬜` / `🔄` → `✅`
- 若已知 URL，则回填为 `✅ <url>`

```bash
python automation/x_publish.py sync-status-to-md
python automation/x_publish.py sync-status-to-md --date 2026-03-18
```

## 为什么暂时不直接写回 Markdown

Markdown 是策划源，不是运行时数据库。

运行态状态单独放：
- `state/publish-state.json`

这样可以避免：
- 误改人工策划文件
- 并发发布时冲突
- 难以回滚

后续如果需要，再增加 `sync-status-to-md` 功能，把 `✅ + URL` 回填到 `x-publish-queue.md`。

## 内容模型

每条内容在执行队列里大致长这样：

```json
{
  "date": "2026-03-18",
  "weekday": "周三",
  "type": "thread",
  "topic": "Serverless DB 迁移 0-1-100",
  "status": "planned",
  "goal": "growth",
  "cta": "RT / follow",
  "asset_type": "diagram",
  "preferred_time": "21:00",
  "source_file": "week-01.md",
  "items": [
    {"index": 1, "kind": "post", "text": "..."},
    {"index": 2, "kind": "reply", "text": "..."}
  ]
}
```

## 配置项

见 `config.example.yaml`。

关键项：
- `account.handle`
- `schedule.default_times`
- `publish.dry_run_default`
- `publish.require_confirm_env`
- `assets.topic_rules`

## NotebookLM 的位置

NotebookLM 更适合：
- 从长文/研究笔记提炼视觉化要点
- 提炼图片 brief

不适合直接“出图”。

因此这里的图片建议生成器先做：
- 统一建议结构
- 生成可供 NotebookLM / 设计工具使用的 brief

未来可以接：
- NotebookLM 摘要输入
- 本地素材目录匹配
- 自动生成图卡文案

## 定时调度建议

### 推荐 cron

- 周一 09:00：发布 Radar
- 周三 21:00：发布 Thread
- 周五 09:00：发布 Radar / 对比卡
- 周日 21:00：发布观点 / 导流

### 运行方式

```bash
python automation/x_publish.py build-queue
python automation/image_suggester.py suggest
python automation/x_publish.py publish --date 2026-03-18 --dry-run
python automation/x_publish.py publish-today --dry-run
```

正式发布：

```bash
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish --date 2026-03-18
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish-today
python automation/x_publish.py sync-status-to-md
```

## 安全策略

- 默认 dry-run
- 只有设置 `X_PUBLISH_CONFIRM=YES` 才允许真实发布
- 若 `xurl auth status` 未通过，直接退出
- 不读取 `~/.xurl`
- 不在日志输出任何敏感凭据

## 下一步建议

1. 先完成 `xurl` 授权
2. 跑一次 `build-queue`
3. 跑一次 `suggest`
4. 先用 `publish --dry-run` 验证本周内容
5. 确认无误后再接 cron / OpenClaw cron
