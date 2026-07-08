# Chuwu PR OS

这是初五的 PR 判断与执行 Skill 包。

当前版本：`chuwu-pr-OS03`

入口目录：

```text
chuwu-pr-OS03/Skills
```

---

## 这是什么

Chuwu PR OS 不是资料库，也不是通用 Prompt 集合。

它是一套面向消费品、公关、传播和舆情工作的 AI Skill 系统，目标是把长期沉淀的公关判断、风险意识、传播框架和执行流程，编译成可重复调用的 AI 能力。

核心原则：

- PR 是业务判断，不只是写稿和发声。
- 信任高于声量，长期高于短期。
- 先判断问题性质，再决定是否动作。
- 输出要减少解释成本，而不是制造更多材料。
- 专项 Skill 负责具体任务，`judgment-hub` 负责最终取舍。

---

## OS03 的主要变化

`chuwu-pr-OS03` 只保留 PR 判断与执行相关 Skill。

上一版中的输入处理和视觉输出能力已从本仓库移除，因为它们是工具型能力，不属于 PR Skills 的核心范围。

已移除：

- `wechat-article-batch-extractor`
- `xiaoyuzhou-live-extractor`
- `frontend-slides`
- `social-card-production`

### 1. 正式判断中枢

```text
chuwu-pr-OS03/Skills/judgment-hub
```

`judgment-hub` 用于处理最终拍板、跨任务分流、风险取舍和策略定性。

它不替代专项 Skill，而是在专项 Skill 完成分析后，回答：

- 要不要回应。
- 要不要发稿。
- 要不要延期。
- 要不要牺牲传播效果保护信任。
- 要不要把外部舆情转成业务自查。
- 哪些动作不该做。

### 2. 执行 Skill 统一转入判断中枢

以下 Skill 已统一改为在关键取舍时转入 `judgment-hub`：

- `copy-lens-review`
- `hot-public-opinion-analysis`
- `media-narrative-analysis`
- `pr-contingency-plan`
- `press-release`

### 3. 新增知识调用地图

每个核心执行 Skill 都有：

```text
references/knowledge-map.md
```

它用于说明该 Skill 应该调用哪些案例、框架、Workflow 和理论作为判断校准。

设计目标不是把知识堆进 `SKILL.md`，而是让 Skill 保持简洁，同时能按需调用更深的知识资产。

### 4. 修复 press-release 路径问题

`press-release` 中原先存在部分规则文件路径不一致的问题。

OS03 已统一为：

- `writing-rules.md`
- `final-review.md`
- `references/types/*.md`

避免执行时查找不存在的规则文件。

---

## Skill 清单

### PR 判断与风险

- `judgment-hub`：公关判断中枢，用于最终拍板、跨任务分流、风险取舍和策略定性。
- `copy-lens-review`：品牌文案上线前的公共语境风险审查。
- `hot-public-opinion-analysis`：热点事件、行业争议、社会话题和负面叙事的舆情研判。
- `media-narrative-analysis`：媒体文章、竞对传播、公关稿和报道的叙事拆解。
- `pr-contingency-plan`：品牌动作上线前的风险地图、舆情预案和对外口径。

### PR 输出生产

- `press-release`：新闻通稿起草、改稿和终稿审查。

---

## 目录结构

```text
chuwu-pr-OS03/
└── Skills/
    ├── judgment-hub/
    ├── copy-lens-review/
    ├── hot-public-opinion-analysis/
    ├── media-narrative-analysis/
    ├── pr-contingency-plan/
    └── press-release/
```

---

## 使用方式

把需要使用的 Skill 放入支持 Skill 的 AI 工作环境中。

优先从具体任务进入：

- 看热点：用 `hot-public-opinion-analysis`。
- 看稿件：用 `media-narrative-analysis`。
- 做预案：用 `pr-contingency-plan`。
- 审文案：用 `copy-lens-review`。
- 写通稿：用 `press-release`。
- 需要最终取舍：用 `judgment-hub`。

---

## 维护原则

- 不因为一次需求就创建新 Skill。
- 相似能力优先合并。
- Skill 应越来越少、越来越稳定、越来越通用。
- 案例、框架、策略和 Workflow 先验证，再沉淀到 Skill。
- 理论只用于校准判断，不替代业务语境和实战判断。

---

## English Summary

Chuwu PR OS is a PR judgment and execution skill package.

OS03 keeps only PR-related skills: judgment, public opinion analysis, narrative analysis, contingency planning, press release drafting, and public-context copy review.

The core idea is simple:

PR is business judgment, not just writing.

Specialized skills handle concrete tasks. `judgment-hub` makes final tradeoffs.
