# 搜索执行、正文验收与定向补证

供`industry-media-research`和`hot-public-opinion-analysis`按需复用，不是新Skill，不触发额外研究范围。已有完整材料时先分析材料；用户要求检索、核验，或关键事实会改变判断时才补搜。简单任务用短记录，多材料任务复用现有底稿，不为套流程新建多份台账。

## 搜索任务与复用

把当前问题转成可执行查询，复杂任务可用下表，共同对象、时间窗和地域只写一次：

`问题／主张ID｜实际查询｜目标来源与材料类型｜需返回字段｜反向或替代查询｜结果／剩余缺口`

先检查已有材料、查询与覆盖窗口，只补缺口；同一材料供多个问题复用。对象别名、产品、品牌、法人和相邻品类分开，扩展材料不得冒充主对象材料。按任务选择来源，不设必跑平台数量；关键词中的年份不能替代逐条发布日期核对。

- 行业媒体研究：围绕功能层、作者署名、同题事件、非发布会报道和反例扩池；记录排序与纳入理由，不只取熟悉媒体或高互动内容。
- 舆情研判：分别查起点材料、回应／更正、传播节点和实际后果；区分本轮最早检出与已确认首发。没有澄清不等于已证实，没有检出不等于没有讨论。
- 当前工具能执行什么，以实际只读调用为准。记录实际工具、查询时间、成功范围和错误；失败时只尝试有依据的可用替代路径，继续其他来源。时间或访问限制与证据充分分别作为停止原因；不重复撞击同一失败入口。

## 逐条内容验收

每条候选复用原有编号，保留标题、发布主体、发布日、原始URL、实际阅读URL和取得时间。取得时间只表示本次获取，不冒充网页实时更新或原始发布日期；缓存结果说明其可见时间边界。

| 字段 | 记录与使用边界 |
|---|---|
| `read_state` | 全文／部分正文／仅摘要／仅元数据／未取得；必须核对目标身份、内容类型、正文边界和截断情况 |
| `saved_form` | 全文／摘录／分析摘要／仅索引／未保存；与实际阅读状态分开，读过全文但仅保存摘要仍可记录全文阅读 |
| `access_state` | 成功／部分／零结果／未登录／访问受限／工具错误／未尝试；不确定原因如实保留，不擅自诊断为封禁 |
| `coverage` | 实际取得的段落、章节、评论排序与层级、分页或视频时段；未处理的图片、附件和字幕单列缺口 |
| `date_state` | 已确认／未显示／冲突；日期未知不能计入已确认时间窗，不能用采集日补齐 |
| `allowed_use` | 当前实际内容支持哪些编码或主张；不能支持的部分明确标出 |

工具返回成功、非空文本、地址栏变化都不足以证明读到目标全文。核对正文中的标题、主体、规范链接或对象ID；导航、推荐列表和错误页不算正文。只取得部分内容时可分析已取得段落，但不推断完整结构、全文立场或未读部分是否缺席；图像缺失仅限制依赖图像的主张，不自动否定可读文字。

搜索摘要只用于发现与定位；已完整阅读的原创文本才计入全文原创样本。日期不明、转载、正文不足的条目保留在候选索引，按具体分析用途另记可用数，不能一并充当有效样本分母。评论未读取时，不从评论数量推导群体态度。互动量保留观察时间，仅在可比口径内使用。

在任务与许可范围内保存必要摘录、摘要和定位；不为验收强制保存全文。原始工具响应和错误若需保留，先脱敏后放当轮`work/`，不进入知识入口或公开交付。

## 按主张识别来源与矛盾

一篇报道可以包含公告、采访和研究者推断，分别定位。沿用`origin_id`／`origin_evidence_id`、`citation_route`和原文位置；同源转载不增加独立事实证据。原始入口未知时写未知，可按已明确归因的同一公告分组，但不能声称已经打开原公告。不同报道的独立采访另行记录，不因部分同源而丢弃整篇。

区分叙事样本、传播节点与独立事实证据：同源内容可说明被怎样转述或在哪些页面出现，不能证明更多独立事件、公众态度或因果。没有阅读量、互动与时间序列时，页面数量也不能冒充传播规模。

先核对是否同一主张、对象、时间、地域、版本、单位和分母。不同对象的数字、承诺与执行、先后阶段变化不自动构成事实冲突。主张强度仍取决于可追溯性、测量匹配、外推边界与替代解释，不使用来源身份总分替代判断。

## 定向补证与回写

仅为会改变核心判断的缺口补证，直接在已有账本或短记录中保存：

`主张ID｜现有版本与来源｜已排除的口径差异｜关键缺口｜目标原文／字段｜完成条件｜补查动作与结果｜处理状态｜受影响判断`

先明确什么材料足以解决问题，再使用当前已授权渠道查原文、定义、时间、方法或更正。已完成的核验不因交给另一个Skill而重做；新增材料重新验收、归因和核对，不能因来自补搜就自动可信。

处理结果使用：

- **已解决**：证据确认错误、版本更新或解释差异；写明采用什么、替代什么。
- **多口径并存**：各自有依据且对象／定义不同，限定范围分别保留，不平均。
- **未解决**：关键依据不足，保留冲突并限制相关结论；可作为有归因的争议内容，不作已证实的前提。
- **拒绝用于该主张**：材料无法支持当前用途，说明原因；不自动禁止其用于有边界的背景或其他主张。

取得证据后同步更新受影响的事实、编码、时间线、结论和交接包；其余已完成判断保持。无法解决时交付缺口和最小下一步，不用新增表格阻塞不依赖缺口的分析或保护动作。

交付检查：推荐材料的阅读与保存状态是否真实；样本／来源计数是否按用途区分；关键冲突是否有处置及结论影响；正文是否保留必要限制。无冲突不创建空台账，不把查询表和制作日志塞进业务正文。

## 来源与适配

初五维护。方法参考hexiaofeier的[tanzi搜索设计](https://github.com/hexiaofeier/tanzi/blob/main/skills/tanzi/references/search-plan.md)、[语料规范](https://github.com/hexiaofeier/tanzi/blob/main/skills/tanzi/references/corpus.md)及[baojie](https://github.com/hexiaofeier/baojie/blob/main/skills/baojie/SKILL.md)，结合本库既有主张级证据与样本规则改写。未引入平台安装依赖、固定调用数量、互动量抽样阈值或S—Z总等级。

上游采用MIT许可，保留声明如下；再分发本参考时保留作者、来源与许可。本文件位于行业媒体研究Skill内，热点舆情Skill通过库内路径复用；单独导出后者时需一并打包此参考并修正链接。

```text
MIT License

Copyright (c) 2026 The tanzi Authors
Copyright (c) 2026 Hehe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
