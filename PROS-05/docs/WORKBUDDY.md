# WorkBuddy上传与调用

## 上传当前压缩包

在当前「配置专家」页面点击「重新上传」，选择`PROS-05-workbuddy.zip`。无需解压或再套一层目录。

本包已补齐专家入口所需的`.codebuddy-plugin/plugin.json`、`agents/chuwu-pros-five.md`和512×512头像`avatars/expert.png`，并在清单中注册原有14项Skill。全部专项方法、参考、脚本和共享资料保持原样，MIT许可及第三方署名保留。

2026-10-15的旧包只有SKILL合集入口，在「配置专家」页面因缺少plugin.json而解析失败。当前同名ZIP已更新为专家格式。此前让用户改选「技能」的说明已撤回；本次修复直接适配用户正在使用的专家上传入口。

## 调用与条件

专家先读取[总入口](../SKILL.md)和[依赖说明](DEPENDENCIES.md)，按当前任务选择专项。最新事实核验需要宿主联网，原始音视频转录需要相应工具。Follow Loop与Skill进化仅在用户明确调用且满足[知识库接入合同](KNOWLEDGE-INTEGRATION.md)时运行。安装不会自动运行脚本或修改知识库。

## 验证范围

已在本地检查ZIP完整性、隐藏配置目录、专家必填字段、Agent定义、头像规格、14项Skill注册路径、包内链接、文件指纹及独立解包。WorkBuddy平台实际解析与审核结果仍以重新上传后的页面为准。

格式依据：[WorkBuddy官方专家文档](https://open.workbuddy.cn/docs/expert)。核对日期：2026-10-15。
