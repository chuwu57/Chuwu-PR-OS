# 依赖与使用范围

## 包内路径

合集根目录是包含总入口`SKILL.md`、`Skills/`和`Domains/`的目录。WorkBuddy安装时应保留它的全部层级。专项的references、assets和scripts相对专项目录；共享Domains和Skills从合集根目录解析。Markdown链接从所在文件目录解析。运行脚本应使用完整实际路径，不能依赖当前工作目录。

共享方法、理论整理及专项之间实际引用的参考已随包保留。私人Evidence、论文全文、案例库、来源账号池、扫描状态、历史运行报告与本机配置没有导出；正文中此类参考已标明未附带。它们不能被当作本次已经读取或已独立核验的证据。

## 14项专项的运行条件

| 专项 | 包内资源与外部输入 |
| --- | --- |
| annual-pr-strategy | 已附总Workflow和两份年度专项Workflow。需用户提供企业任务、资源、责任和数据；不足时交付有明确待补项的工作稿。 |
| copy-lens-review | 已附视角、风险、宠物食品参考和Python词语初筛。需完整文案与语境；脚本只定位信号，不代替判断。 |
| hot-public-opinion-analysis | 已附知识地图、证据策略和共享采集参考。材料内分析可直接做；当前传播状态及冲突事实核验需联网证据。 |
| judgment-hub | 已附决策门和交接协议。需有依据的事实、备选动作与组织约束；不自动变成每个任务的必经步骤。 |
| media-narrative-analysis | 已附媒体信号及叙事框架。需文章原文及来源；全文不可访问时保留覆盖范围。 |
| pr-consumer-research | 已附购买路径转换、统计主张等跨Skill参考。需要已有研究；没有数据时不能生成实证结果。 |
| pr-contingency-plan | 已附场景参考与Workflow。需尚可调整的动作事实、范围和组织条件。 |
| press-release | 已附稿型参考与模板。需真实企业事实、引语授权及公开范围。 |
| consumer-research | 已附研究情境、VOC、统计与消费场景等参考。可以设计研究；实际洞察需要真实数据，不模拟消费者作答冒充研究。 |
| industry-media-research | 已附编码和采集参考。需要可读取文章样本；搜索命中不等于全文已读。 |
| industry-research | 已附报告模板、证据CSV与审计脚本。联网研究及外部数据权限由宿主提供；审计不证明事实正确。 |
| follow-loop | 需使用者兼容知识库、来源登记、状态、目标资产目录和校验工具。按[接入合同](KNOWLEDGE-INTEGRATION.md)部署；安装本包不等于已接入。 |
| spoken-content-extractor | 现成转录可直接提取。原始音视频需转录能力；本地脚本需faster-whisper及模型，未随包分发。索引脚本使用Python标准库。 |
| skill-evolution | 需用户指定的维护目标、知识库规则、注册、版本及真实反馈／任务证据。缺失时先做只读盘点或提出待验证任务，不宣称已经提升能力。 |

## 脚本环境

Python脚本建议Python 3.10或以上；Follow Loop部分校验使用Path.is_relative_to（Python 3.9或以上），统一采用3.10＋可减少差异。3份Ruby脚本使用Ruby标准库yaml/date。普通Markdown任务无需安装这些运行时。

运行前先读脚本帮助或接口；不因安装自动执行。转写的faster-whisper、模型下载和来源访问权限由使用者按实际环境配置。未在Windows或WorkBuddy实际运行脚本，不声称已经通过跨平台运行测试。
