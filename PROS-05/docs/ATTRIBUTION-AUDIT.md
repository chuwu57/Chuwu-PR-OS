# PROS 05归属与分发自检

审查日期：2026-10-15。范围：14项Skill的正文、description、已有agents界面配置、运行参考／模板／脚本、共享方法、总入口、README和版权／许可说明。源知识库未修改；修正只发生在本地分发副本。

## 发现及处理

1. **统一许可缺失**：OS04公开版权说明确实没有统一开源许可证。此次已准备并经初五确认开源发布，正式加入MIT全文；适用范围见开源许可说明。
2. **上游许可依据需要说准确**：Follow Loop的原说明写「上游声明许可证MIT」。只读核对登记的follow-builders提交，README声明MIT，但没有独立LICENSE。分发版明确这一区别，保留作者／仓库／基线与方法改造范围，不补造上游版权人或原始许可文件，也不复制上游代码、原始Prompt或文档正文。
3. **引用许可证随包性不足**：焦点小组参考已有上游链接和作者说明，但未附MIT全文。现补入qualitative-research-skill contributors的原许可；tanzi与baojie原文内已有声明，再补独立原许可文件，便于分发时保持完整。
4. **个人路径与资源引用**：年度战略的固定根路径改为包内解析；Follow Loop和skill-evolution明确使用者知识库根。消费者研究原有两处个人文章路径改为已附竞品研究框架与证据参考；私人底稿只保留来源标签与未附带说明，不把不存在的文件作为已经读取的依据。
5. **个人来源池与历史**：Follow Loop只保留可复用采样规则；固定个人栏目选择改为使用者登记，真实Sources、State、Case历史与运行报告均未导出。
6. **没有发现的情况**：14项入口没有把初五维护归到其他作者；界面短描述未发现其他项目作者冒名或未替换占位作者。学术作者、真实品牌示例及4项真实上游项目属于必要来源，不作为模板残留删除。

## 逐项结果

| Skill | 入口归属 | 特别核对 |
| --- | --- | --- |
| annual-pr-strategy | 初五维护；description与正文一致 | 未发现误署其他作者 |
| copy-lens-review | 初五维护；description与正文一致 | 未发现误署其他作者 |
| hot-public-opinion-analysis | 初五维护；description与正文一致 | 保留tanzi／baojie共享参考及MIT全文 |
| judgment-hub | 初五维护；description与正文一致 | 未发现误署其他作者 |
| media-narrative-analysis | 初五维护；description与正文一致 | 未发现误署其他作者 |
| pr-consumer-research | 初五维护；description与正文一致 | 未发现误署其他作者 |
| pr-contingency-plan | 初五维护；description与正文一致 | 未发现误署其他作者 |
| press-release | 初五维护；description与正文一致 | 未发现误署其他作者 |
| consumer-research | 初五维护；description与正文一致 | 保留qualitative-research-skill来源及MIT全文 |
| industry-media-research | 初五维护；description与正文一致 | 保留tanzi／baojie共享参考及MIT全文 |
| industry-research | 初五维护；description与正文一致 | 未发现误署其他作者 |
| follow-loop | 初五维护；description与正文一致 | 保留follow-builders来源；细化MIT声明边界 |
| spoken-content-extractor | 初五维护；description与正文一致 | 未发现误署其他作者 |
| skill-evolution | 初五维护；description与正文一致 | 未发现误署其他作者 |

## 归属结论的边界

本次确认所分发版本的维护归属表述、显式来源和已找到的许可信息一致；无法从文件扫描证明所有历史表达均由某人原创。因此统一写「初五整理、维护或改造」，不写「14项全部由初五原创」。来源指纹说明版本一致性，不证明著作权。

保留的第三方声明见NOTICE及licenses。理论笔记保留研究者归属，论文全文与私人证据底稿不分发。本版本正式包含MIT LICENSE，不能被解读为旧版本已一直采用该许可。
