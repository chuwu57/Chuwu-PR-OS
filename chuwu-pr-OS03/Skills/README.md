# Skills

Skills 是 AI 能力资产，不是知识本身。

本目录只保留 PR 判断与执行相关 Skill。

输入处理、视觉输出、通用内容生产等工具型能力不放在这个 GitHub 版本中。

---

# 每个 Skill 的最低结构

```text
Skill-Name/
├── SKILL.md
├── Feedback.md
├── Changelog.md
└── Test-Cases/
```

---

# 管理原则

- 不因为一次需求就创建新 Skill。
- 相似 Skill 应优先合并。
- Skill 应越来越少、越来越稳定、越来越通用。
- 修改 Skill 前，先记录 Feedback，再积累案例，再修改。
- 每次修改后，应补充 Test Case 并验证。
- 理论、案例和框架用于校准判断，不替代业务语境和实战判断。

---

# 当前 Skill 清单

## PR 判断与风险

- `judgment-hub`：公关判断中枢，用于最终拍板、跨任务分流、风险取舍和策略定性。
- `copy-lens-review`：品牌文案上线前的公共语境风险审查。
- `hot-public-opinion-analysis`：热点事件、行业争议、社会话题和负面叙事的舆情研判。
- `media-narrative-analysis`：媒体文章、竞对传播、公关稿和报道的叙事拆解。
- `pr-contingency-plan`：品牌动作上线前的风险地图、舆情预案和对外口径。

## PR 输出生产

- `press-release`：新闻通稿起草、改稿和终稿审查。

---

# OS03 范围说明

OS03 不包含以下工具型 Skill：

- `wechat-article-batch-extractor`
- `xiaoyuzhou-live-extractor`
- `frontend-slides`
- `social-card-production`

原因：它们分别属于输入处理、资料抽取、视觉表达或固定样式输出，不属于本仓库要对外展示的 PR 判断与执行 Skill。
