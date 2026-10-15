# PROS 05｜初五的公关、研究与知识维护Skill合集

PROS 05由初五整理维护，包含14项Skill：8项公关、3项研究、3项知识与维护。它将公关工作中需要反复判断的问题，整理为Agent可按任务读取的方法、参考资料、模板和辅助脚本。

从真实材料与业务问题出发，先分清事实、解释与假设，再形成可审阅的分析、研究、方案或文稿。资料不够时说明缺口，不虚构企业事实、消费者回答或研究结果。

当前版本：5.0.0｜2026-10-15｜MIT开源。

## PROS 05的主要更新

- 消费者研究与PR转化补充购买过程、搜索、售后、低频消费、文化趋势及焦点小组等场景判断，并加强统计主张、人群外推与业务承接边界。
- 舆情与研究流程补充主张级证据核对、跨来源分歧、正文覆盖及定向补证；检测和实测争议要先对齐问题、对象与工况。
- 新增skill-evolution，依据知识积累与真实任务反馈维护已有Skill，保存版本、核对改动并验证变化。由用户明确启动，不自动在后台自我进化。

相对公开OS04，原13项中10项涉及方法／流程／知识调用，1项包含运行校验修复，2项主要对齐入口说明。逐项变化与验证边界见[版本说明](PROS-05/CHANGELOG.md)。

## 选择适合当前任务的Skill

| 专项 | 调用名 | 解决的问题 |
| --- | --- | --- |
| 全年公关战略 | `annual-pr-strategy` | 年度媒体关系、舆情管理或综合公关战略 |
| 文案公共语境审查 | `copy-lens-review` | 广告、社媒与短文案的公共语境风险 |
| 热点舆情分析 | `hot-public-opinion-analysis` | 已经进入公共讨论的热点、争议与风险 |
| 公关判断中枢 | `judgment-hub` | 分析后仍待决定的回应、优先级与代价 |
| 稿件叙事分析 | `media-narrative-analysis` | 单篇文章的叙事选择、认知效果与意图假设 |
| 消费者证据PR转化 | `pr-consumer-research` | 把已有研究转成可公开主张和业务动作 |
| 公关预案 | `pr-contingency-plan` | 尚未上线动作的风险地图、口径与准备 |
| 新闻通稿 | `press-release` | 通稿起草、改写与正式发布前终审 |
| 消费者研究 | `consumer-research` | 研究方案、题纲、问卷、VOC与洞察报告 |
| 行业媒体研究 | `industry-media-research` | 行业在媒体中的议题、证据与叙事差异 |
| 行业研究 | `industry-research` | 行业进入、竞争、价值链及经营条件研究 |
| Follow Loop情报更新 | `follow-loop` | 明确调用后的五线增量情报与知识写入 |
| 口述内容提取 | `spoken-content-extractor` | 音视频、播客、演讲与转录的内容提取 |
| Skill进化与维护 | `skill-evolution` | 明确调用后依据知识与反馈维护已有Skill |

完整输入、交付、改动与验证范围见[14项Skill明细](PROS-05/docs/SKILLS.md)。

## 如何使用

在支持SKILL.md的Agent工具中读取对应专项，或通过WorkBuddy合集入口按任务调用。先看[依赖与使用范围](PROS-05/docs/DEPENDENCIES.md)，保留完整目录；只复制SKILL.md会丢失参考和脚本。

例如：「使用PROS 05的press-release，根据这些事实写一篇新品通稿；未确认内容保留待补项。」或者：「使用consumer-research，为售后体验设计访谈题纲；目前没有样本数据。」

WorkBuddy版已适配「配置专家」入口，包含专家配置、Agent入口、头像和原有14项Skill。[下载WorkBuddy上传包](https://github.com/chuwu57/Chuwu-PR-OS/raw/refs/heads/main/downloads/PROS-05-workbuddy.zip)，上传方式见[WorkBuddy说明](PROS-05/docs/WORKBUDDY.md)。

普通材料分析与文稿按实际输入执行；最新事实核验需要联网工具，原始音视频转写需要相应运行依赖。Follow Loop与skill-evolution需要使用者知识库、配置及授权，详见[知识库接入合同](PROS-05/docs/KNOWLEDGE-INTEGRATION.md)。安装不会自动创建定时任务或修改知识库。

## 文件与验证范围

包含14项专项说明、参考、模板、辅助脚本和所需共享方法。不包含私人原始材料、个人账号来源池、扫描状态、历史运行记录、完整论文语料或初五的完整知识库。

本次分发检查验证包结构、路径、文件指纹和代表辅助脚本；尚未完成本版本在WorkBuddy专家入口的实际解析与导入、全部14项真实业务任务、在线采集和音频转写验证。既有真实任务、受控模拟与静态审读的证据强度不同，不统一包装为效果提升。详见[检查报告](PROS-05/docs/PACKAGE-CHECK.md)。

## 开源与归属

初五有权许可的内容采用[MIT许可](LICENSE)，允许使用、修改、商用与再分发，并保留版权及许可声明。适用范围见[开源许可说明](PROS-05/docs/LICENSE.md)。第三方方法、理论和工具仍保留真实来源，见[NOTICE](PROS-05/NOTICE.md)。

仓库：[chuwu57/Chuwu-PR-OS](https://github.com/chuwu57/Chuwu-PR-OS)。此前OS04的历史保留在Git提交记录中。
