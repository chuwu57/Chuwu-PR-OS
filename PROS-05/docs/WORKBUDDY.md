# WorkBuddy技能合集：上传入口与调用

## 使用「技能」入口

本包是一个Skill合集，应在WorkBuddy开放平台的「技能」发布入口创建或更新。上传文件：`PROS-05-workbuddy-skill.zip`。ZIP根目录直接包含`SKILL.md`，内部保留14项专项方法与共用资源，不要再套一层目录。

如果当前页面标题是「配置专家」，请返回并选择「技能」。专家入口要求`.codebuddy-plugin/plugin.json`、Agent定义及专家展示配置；本Skill包不包含这些文件，不能上传到专家入口。平台报「未找到.codebuddy-plugin/plugin.json」表示上传类型不匹配，处于解析阶段，不是内容审核驳回。

上次OS04使用的是Skill合集结构。本次依据旧结构准备了同类包，但此前上传说明没有明确区分专家和技能入口。2026-10-15根据用户的实际报错补充这一说明，并将下载文件名改为明确的`workbuddy-skill`。14项专业方法未因此改变。

## 上传步骤

1. 回到开放平台发布入口，选择「技能」，创建或更新对应技能。
2. 上传`PROS-05-workbuddy-skill.zip`，无需解压再压缩。不要上传宣传图文ZIP或整个交付目录。
3. 等待平台解析`SKILL.md`及元数据，再检查显示信息。只有平台实际显示解析成功，才算通过这一步；后续提交与审核状态另行确认。

原`PROS-05-workbuddy.zip`下载地址作为兼容别名保留，两者内容相同。它也属于技能包，不能用于「配置专家」。

## 元数据与运行

总入口保留name、display_name、display_name_en、description、description_zh、description_en、version与author。显示名为PROS 05，机器标识为chuwu-pros-05，版本字段为5.0.0。安装列表显示一个合集，内部按任务读取14项专项方法。

示例：

- 「使用PROS 05的press-release，根据这些真实材料写新品通稿，缺少事实保留待补项。」
- 「使用PROS 05的consumer-research，设计售后体验研究，暂时不要生成研究结果。」
- 「使用PROS 05的skill-evolution，检查指定Skill能否采用这份反馈，先核对知识库接入条件。」

Follow Loop和Skill进化仍需使用者知识库、配置及授权，见[知识库接入说明](KNOWLEDGE-INTEGRATION.md)。

## 验证边界与官方依据

本次完成本地ZIP、元数据、相对路径与代表脚本检查。用户反馈的专家入口上传已发生解析失败；尚未验证本版本在技能入口实际解析、导入或审核通过。

- [官方技能格式](https://open.workbuddy.cn/docs/skill)：以SKILL.md定义技能。
- [官方专家格式](https://open.workbuddy.cn/docs/expert)：以.codebuddy-plugin/plugin.json及Agent定义配置专家。

核对日期：2026-10-15。是否选择专家形式属于另一种发布需求，不能仅为消除报错就把Skill合集改为专家或专家团。
