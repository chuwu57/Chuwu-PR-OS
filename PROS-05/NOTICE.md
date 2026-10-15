# 第三方来源与改造范围

PROS 05由初五整理、维护。以下项目名和作者属于真实来源，必须保留。

| 来源 | 本包涉及位置 | 改造范围与许可 |
| --- | --- | --- |
| Zara Zhang／zarazhangrui的[follow-builders](https://github.com/zarazhangrui/follow-builders) | Follow Loop的ai-knowledge-contract | 借鉴关注建设者及原始来源核验思路，重构为知识库增量维护。未复制上游代码和原始Prompt。上游README声明MIT，指定提交没有独立LICENSE，见[来源说明](licenses/follow-builders-source.md)。 |
| hexiaofeier的[tanzi](https://github.com/hexiaofeier/tanzi) | 行业媒体研究、热点舆情共用的collection-and-evidence-review | 参考搜索设计与语料验收，结合主张级证据规则改写；保留The tanzi Authors的[MIT全文](licenses/tanzi-MIT.txt)。未引入其平台脚本或抓取器。 |
| hexiaofeier的[baojie](https://github.com/hexiaofeier/baojie) | 同上 | 参考采集与补证方法，保留Hehe的[MIT全文](licenses/baojie-MIT.txt)。没有采用上游全套流程。 |
| [qualitative-research-skill](https://github.com/maydengximin-sketch/qualitative-research-skill) contributors | 消费者研究的focus-groups-and-social-meaning | 参考群体互动、主持及个人／小组分析区分，由初五重新组织；保留[MIT全文](licenses/qualitative-research-skill-MIT.txt)，不采用固定样本数量与饱和门槛。 |

共享理论笔记属于初五的整理与应用性解释；理论提出者及文献作者仍按正文归属。论文全文、书籍语料和私人核验底稿不在包内；需要使用具体研究结果时应回到原始文献。

Python、Ruby和可选的faster-whisper是外部运行依赖，未随包复制其代码或模型。本包不包含logic-ui、logic-charts、Hallmark或其模板，宣传视觉不构成新增公开Skill。
