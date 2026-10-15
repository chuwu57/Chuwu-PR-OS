# 使用者知识库接入合同

## 三种路径不要混用

- 包内共享方法：从PROS 05合集根目录读取。
- 使用者知识库：`PR_KNOWLEDGE_ROOT`指向用户明确授权的目录，仅在Follow Loop或skill-evolution接入时使用。
- 当前任务：输入与临时文件放用户任务目录，交付放outputs；不把安装目录当成任务缓存。

变量名只代表路径约定，安装不会自动设置。macOS／Linux可先执行`export PR_KNOWLEDGE_ROOT="/absolute/path/to/your/knowledge-base"`；PowerShell可使用`$env:PR_KNOWLEDGE_ROOT = 'C:\path\to\knowledge-base'`。将示例换成真实目录后再执行。Agent应核对变量实际值与用户授权，不能把字面`${PR_KNOWLEDGE_ROOT}`当作已存在目录。

## Follow Loop：完整运行的接入条件

本版保留原脚本的目录定位方式。将包内`Skills/Knowledge-Intelligence/follow-loop/`部署到使用者知识库的同一路径，并保留该目录中的references、scripts和精简Feedback。三个Ruby脚本从该目录向上定位知识库；Python检查器可显式传`--root`。不要在未部署的插件安装目录直接跑完整Harness。

所需接口：

1. 根目录规则、README、Skills/README和registry。注册表应有`follow-loop`及路径`Skills/Knowledge-Intelligence/follow-loop`。旧校验器会核对入口中的「启动Follow Loop，更新一下」「FL一下」；只在使用者同意设置这两个触发词时同步到其入口。
2. `Domains/PR/45-Workflows/Workflow_Follow-Loop.md`：可采用本包提供的合同，先与使用者现有规则核对。
3. `Domains/PR/90-System/Follow-Loop/`中的Config.yml、Topics.yml、Sources.yml、State.md、Case-State.yml以及Runs目录。来源由使用者选择，初始窗口由使用者明确；不得伪造扫描历史。Config中的别名字段须符合脚本合同。
4. AI人物、PR人物与信号、Case候选、具身智能、奢侈品的资产与Evidence目录。各文件最低结构见本Skill对应lane参考，目录路径见routing-and-write-contract。
5. 使用者知识库检查器。原契约以`.codex/checks/kb_check.rb`为入口；没有该检查器时先建立适合其知识库的检查，不假报`kb_check=passed`。
6. 实际可用的公开来源访问／检索工具、Python与Ruby，以及明确的写入授权。

来源状态字段与manifest格式见包内参考及脚本。示例源使用`active: false`，不能用示例域名制造有效数据或推进断点。包内不提供初五来源池、State或Case历史，也不会用空文件伪造五线已就绪。

接入完成后，先保存真实状态基线；部署目录中运行`python3 scripts/test_follow_contract.py`检查隔离行为，再在使用者库中执行实际Harness。真实运行仍须完成来源覆盖、Evidence核验和各lane验收；隔离测试通过不等于采集或写回完成。

缺失时：列出缺失文件／工具、受影响lane及最小恢复步骤；可以准备来源候选和配置建议，不采集写回、不推进水位、不声称「本轮无新增」或「五线通过」。已有授权且依赖齐全的独立部分可继续。

## skill-evolution：维护接入条件

指定要维护的已有Skill与可写范围，读取使用者根及子目录规则、注册表、目标当前工作树、相关知识与来源Workflow、Feedback及Test-Cases。未采用本包目录体系的知识库应先把注册与检查接口映射清楚；不要自动重建一套PR Knowledge OS。

本包附任务记录模板和验证说明，不附初五的真实任务记录。目标缺反馈时标「没有真实反馈」，可进行静态诊断；缺知识时说明最关键的依据缺口。没有证据支持修改，交付「保留原版」也是有效结果。

修改前备份真实工作树及依赖，记录指纹，并在写入前复核并发变化。先按任务影响完成验证，再记录采用、撤销、保留或观察。只在已授权范围写入；不新增技能、不安装外部Skill、不自动运行Follow Loop、不创建后台自动进化。

## 本包提供的范围

提供14项方法、共享规则与可独立运行的辅助脚本；完整知识库采集／维护依赖使用者接入。接入前仍可阅读方法、执行普通材料分析及使用不依赖知识库的工具，不把缺少私人知识库误写为所有Skill不可用。
