# OpenClaw Cron 调度方案

## 目标

让 `@Cloud_Neutral` 的发布流程按计划自动运行：

1. 每天定时构建可执行队列
2. 生成图片建议
3. 到发帖时间执行 dry-run 或正式发布
4. 发布后记录状态

## 推荐调度

### 每天早上 08:30
- 重建发布队列
- 重建图片建议

```bash
python automation/x_publish.py build-queue
python automation/image_suggester.py suggest
```

### 周一 09:00
- 发布 Radar

```bash
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish --date 2026-03-16
```

### 周三 21:00
- 发布 Thread

```bash
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish --date 2026-03-18
```

### 周五 09:00
- 发布 Radar / 对比卡

### 周日 21:00
- 发布观点 / 导流

## OpenClaw cron 设计

更推荐两层任务：

### A. 每日构建任务
- 时间：每天 08:30
- 动作：构建队列 + 生成图片建议

### B. 发布任务
- 每个发帖时点单独一个 job
- job 内容只做：
  - 根据当天日期定位条目
  - 执行发布

## 为什么不把日期写死在命令里

已经支持：

```bash
python automation/x_publish.py publish-today
```

逻辑：
- 根据当前 Asia/Shanghai 日期
- 在 `publish-queue.json` 里找当天条目
- 自动执行 dry-run / publish

这样 cron 配置更简单。

## 当前可直接落地的 cron 思路

### 任务 1：每日重建队列
- cron: `30 8 * * *`
- 命令：

```bash
python automation/x_publish.py build-queue && python automation/image_suggester.py suggest
```

### 任务 2：周一发布
- cron: `0 9 * * 1`
- 命令：

```bash
X_PUBLISH_CONFIRM=YES python automation/x_publish.py publish-today && python automation/x_publish.py sync-status-to-md
```

### 任务 3：周三发布
- cron: `0 21 * * 3`

### 任务 4：周五发布
- cron: `0 9 * * 5`

### 任务 5：周日发布
- cron: `0 21 * * 0`

### OpenClaw 可导入方案

见：
- `automation/openclaw-cron-jobs.json`

其中包含：
- 每日 build job
- 周一 / 周三 / 周五 / 周日发布 job

## 发布前建议

在正式自动发之前，先跑 1 周 dry-run：

```bash
python automation/x_publish.py publish --date 2026-03-18 --dry-run
```

确认这些都正确：
- 日期映射正确
- thread 顺序正确
- CTA 正确
- topic 对应内容正确
- 图片建议匹配内容类型

## 后续增强

1. `publish-today`
2. `sync-status-to-md`
3. `publish-next`
4. `retry-last-failed`
5. `notebooklm-brief`：把素材提炼成图卡 brief
