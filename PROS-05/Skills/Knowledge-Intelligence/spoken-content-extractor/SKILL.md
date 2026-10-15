---
name: spoken-content-extractor
description: "初五的口述内容提取Skill。处理播客、直播回放、演讲／访谈视频、音频、现成转录或节目文稿，按任务选择知识增量、定点核验或全量转写，交付转录、内容简报、学习指南或PR素材，并说明实际覆盖范围。知识库写回须有用户授权；普通文章分析、视频剪辑和仅需播放链接不使用本Skill。"
---

# Spoken Content Extractor

> 归属说明：本Skill由初五维护，属于初五的个人Skill体系。分享或再分发时请保留本归属说明及已有来源、作者和许可声明。

## Core Rule

Work only from materials the user can access or has provided. Do not bypass paywalls, private rooms, login-only content, anti-scraping controls, DRM, or platform restrictions. If a link cannot be accessed directly, ask for an exported audio file, copied page text, transcript, show notes, or another accessible source.

## Artifact Placement

Keep execution material and knowledge assets separate from the start:

- **Working layer:** downloaded audio, temporary dependencies, ASR Markdown, JSONL, logs and inspection files go under the current task's `work/`. They are not active knowledge-base content.
- **Source preservation:** only when the user asks to preserve source material for future verification, place original audio and full transcript in the appropriate `Archive/` or `60-References/` location, with provenance and access boundary. Do not place copyrighted full text in an active knowledge entrypoint.
- **Active knowledge layer:** when the user explicitly asks to absorb the episode into the knowledge base, write only evidence-backed facts, short verified quotations, structured Reading or a reusable framework/case. Link to the preserved evidence record; do not copy the full ASR transcript into Domains, README or MOC.
- **No automatic write-back:** extraction, brief and learning-guide requests stay in task outputs unless the user explicitly asks for knowledge-base absorption.

## Mode Gate

Choose the least expensive mode that can support the requested conclusion. Accessible audio is not, by itself, a reason to run full ASR.

1. **Knowledge-increment mode — default for「吸收、归档、看看什么值得入库、提炼长期判断」:**
   - Inspect public metadata, detailed show notes, timeline, linked primary material, and existing knowledge assets first.
   - State the「新增回答的问题」before transcription. If the episode adds no mechanism, evidence, state, boundary, or action, link it as supporting evidence or skip write-back.
   - Use show notes and targeted verification where sufficient. Mark the Evidence `partial` and disclose coverage when part of the episode has not been transcribed or heard.
2. **Targeted-verification mode — default when one or more pivotal claims need audio support:**
   - Use the timeline to transcribe only the relevant windows, normally 2–5 minutes around each target.
   - Verify exact wording against the audio before quoting. Do not upgrade a targeted sample into a whole-episode conclusion.
3. **Full-transcript mode — use only when:**
   - the user explicitly asks for a complete transcript, complete episode summary, or full-coverage study guide;
   - exact quotation coverage across the whole episode is required; or
   - usable show notes/transcripts are absent and the requested conclusion genuinely requires whole-episode coverage.

For multiple episodes, triage every page and test novelty before starting ASR. Do not run two CPU transcription jobs in parallel by default.

## Intake Decision

Identify the available source and proceed with the strongest path:

- Public spoken-content page: inspect HTML/page metadata for accessible audio or video, show notes, title, date, duration, speakers and timeline. On Xiaoyuzhou episode pages, also look for schema.org `associatedMedia.contentUrl` and `og:audio`.
- Audio or video file: choose targeted or full transcription according to the Mode Gate.
- Existing transcript: use it directly; keep original timestamps if present.
- Show notes only: produce a show-note-based brief and clearly say it is not a full transcript.
- Multiple sources: keep source labels and reconcile conflicts conservatively.

Ask for confirmation only when access, copyright, or output purpose is ambiguous.

## 说话人与表达归属

多人材料先核对说话人标签与实际人物的对应依据；标签含混、交叠发言或转录分段混合时，保留不确定性，不凭一次附和认定观点作者。提问者的概括、其他参与者的观点、本人明确判断与后续AI命名分别归属；转述别人的话也不能自动成为转述者的主张。

可发布表达区分逐字摘录、忠实润色与延伸总结。跨段合并、增加条件或提出新概念属于编辑加工，不能倒标为本人原话。每条保留可回到原段的时间码或定位；原文没有时间码时不补造。仅有转录时说明「据转录摘录，未回听」，不声称逐字音频核验。

作者不确定的句子不作为指定人物原话使用，继续处理归属明确的材料。发布版可用一行整体编辑说明，逐条出处与加工类型保留在溯源版；不把考据注释强塞进用户要求的纯语录正文。

## Execution References

Before any audio transcription, read [transcription-and-index.md](references/transcription-and-index.md) for the runtime sample, transcription commands and coverage checks. Before comprehensive analysis of a long full transcript, read its indexing workflow: verify source hashes and complete segment coverage, process all chunks in order into an evidence map, and reuse that map for follow-ups. Keyword search alone cannot establish whole-episode coverage or absence.

Full transcripts must be checked against source duration, beginning and tail; targeted work must declare checked windows. Keep ASR and indexes under `work/`. A requested full transcript remains a full-coverage task even if the runtime estimate is long.

## Output Defaults

For extraction/summarization:

```markdown
## 基本信息
## 一句话结论
## 核心摘要
## 主题脉络
## 关键观点
## 可引用表达
## 适合二次传播的素材
## 风险与待核实点
```

For learning/study requests, read `references/study-guide-patterns.md` and produce a study guide with:

- top-level learning conclusion
- what to learn
- timestamped highlights
- concept explanations
- knowledge map
- application questions
- reference readings
- second-listen plan

Use Chinese by default for Chinese-language podcast content.

## Quality Bar

- Separate verbatim transcript lines from paraphrased highlights.
- Keep timestamps whenever the transcript has them.
- Flag uncertain automatic transcription terms as "待核实".
- Label show-note-only and targeted-transcription Evidence as `partial`; state exactly which ranges or claims were checked.
- Do not invent sources or references; if browsing, prefer primary/credible sources.
- When quoting from transcript/audio, keep quotes short and grounded in the generated transcript.
- For learning guides, focus on transfer: how the user can use the knowledge in work, judgment, writing, strategy, or personal growth.
- Before writing to the knowledge base, confirm that the output is a durable Evidence, Reading, case or framework rather than a transcript, run note or temporary file.

## References

- Read `references/output-patterns.md` for content briefs, PR/media notes, and social repurposing.
- Read `references/study-guide-patterns.md` for learning guides, highlights, reference lists, and knowledge-application outputs.

## 分发版路径与运行条件

先读取[依赖说明](../../../docs/DEPENDENCIES.md)。本Skill由初五维护；本副本为PROS 05。`references/`、`assets/`和`scripts/`相对本Skill目录解析；`Domains/`、`Skills/`前缀从合集根目录解析。包内Markdown链接相对所在文件解析。未附带的个人案例、文献底稿、状态与来源配置只能由使用者提供，不能声称已读取。
