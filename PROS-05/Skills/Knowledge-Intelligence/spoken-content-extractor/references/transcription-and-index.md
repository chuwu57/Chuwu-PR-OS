# Transcription, Coverage and Indexing

Read this file before downloading/transcribing audio or analyzing a long full transcript. Paths under `scripts/` are relative to the Skill root.

## Speed Budget

- Abandon a page-loading path after about 30 seconds without useful progress; switch to public HTML, metadata, show notes, or a user-provided file.
- Before a long local ASR run, test a 3–5 minute clip. If projected runtime exceeds 15 minutes per episode or half the audio duration, use targeted verification for knowledge-increment tasks. For an explicitly requested full transcript, report the estimate before continuing.
- Prefer batched decoding with beam size 1 on CPU. Increase beam size or model size only for a named accuracy problem.
- Give the user a progress update at least every 60 seconds during long work. Stop or change strategy when the same path is not producing useful evidence.

## End-to-End Workflow

1. Create a `work/` folder for artifacts when the task is more than a short answer; do not use a Skill directory or an active knowledge directory as scratch space.
2. Preserve provenance: title, podcast/show, host/guest if available, URL/file, duration, date, source type, and access notes.
3. Select a mode and run the novelty test before downloading or transcribing long audio.
4. Extract accessible audio only when the selected mode needs it:
   - Prefer public metadata fields such as `og:audio` or `associatedMedia.contentUrl`.
   - Download only public audio URLs exposed by the page.
   - Keep the original audio in `work/` while processing. Preserve it beyond the task only under the source-preservation rule above.
5. Transcribe audio:
   - Prefer `scripts/transcribe_audio.py` for local timestamped transcript generation.
   - If local transcription dependencies are unavailable, install them under the current task's `work/` folder or ask the user for permission/alternative only when needed.
   - For targeted verification, record every processed time window and do not label the result「完整逐字稿」.
   - For full transcription, produce both Markdown and JSONL when possible.
6. Verify coverage:
   - For full transcription, check audio duration against the final transcript timestamp, plus file size, segment count, beginning, and tail.
   - For targeted transcription, verify only the declared windows and retain a `partial` evidence boundary.
   - Note that automatic transcripts can misrecognize names and technical terms.
7. Index long full transcripts before analysis:
   - Run`scripts/index_transcript.py build`on the timestamped JSONL, then run`verify`; keep the index and chunks in the task's`work/`folder.
   - For the first comprehensive output, process every indexed chunk exactly once in order and write a compact evidence map with chunk ID, time range, speakers, themes, claims, facts, quote candidates, and uncertainties. Build the final answer from that map; reopen source chunks only for exact quotations or fact checks.
   - For follow-up questions or new repurposing, search the index and evidence map first. A change of audience, language or output format reuses the complete evidence map. If a new whole-episode question needs a dimension absent from that map, review all chunks for that missing dimension; do not treat partial keyword matches as proof that a theme is absent. Preserve source hashes and coverage so unchanged evidence is not reread without a reason.
8. Extract and study:
   - Build a structured brief from the transcript.
   - Highlight key passages with timestamps.
   - Explain concepts, frameworks, and assumptions.
   - Convert ideas into practical questions and reusable checklists.
   - Add credible reference readings when the user asks to learn or apply the content.
9. Repurpose only after extraction: create PR notes, social posts, newsletter copy, internal briefings, or learning materials from transcript-grounded content, not guesses.
10. Before any knowledge-base write-back, classify each artifact using the Artifact Placement rule. Full transcript and JSONL never become an active knowledge entrypoint.

## Local Transcription Script

Use `scripts/transcribe_audio.py` for long audio when a local transcript is needed.

Example:

```bash
python3 -m pip install --target work/.deps-fw faster-whisper
PYTHONPATH=work/.deps-fw python3 /path/to/skill/scripts/transcribe_audio.py \
  --audio episode.m4a \
  --title "节目标题" \
  --source-url "https://www.xiaoyuzhoufm.com/episode/..." \
  --model small \
  --language zh \
  --beam-size 1 \
  --batch-size 8 \
  --out-prefix episode-transcript \
  --prompt "中文商业播客，涉及品牌、营销、AI、CLV、ROI。"
```

For targeted verification, bound the requested window:

```bash
PYTHONPATH=work/.deps-fw python3 /path/to/skill/scripts/transcribe_audio.py \
  --audio episode.m4a \
  --clip-start 1140 \
  --clip-end 1440 \
  --out-prefix episode-19m-to-24m
```

Prefer `small`, CPU `int8`, beam size 1, and batched decoding for speed. Use `medium` or a larger beam only for a named accuracy problem. For long Chinese podcasts, include a domain prompt with likely names, terms, and English acronyms.

## Transcript Index

The index reduces repeated transcript loading; it never replaces the full transcript. Build and verify it after JSONL transcription:

```bash
python3 /path/to/skill/scripts/index_transcript.py build \
  --jsonl work/episode-transcript.jsonl \
  --out-dir work/episode-index \
  --chunk-seconds 300
python3 /path/to/skill/scripts/index_transcript.py verify \
  --index work/episode-index/index.json
```

For a follow-up, retrieve a small candidate set before opening source chunks:

```bash
python3 /path/to/skill/scripts/index_transcript.py search \
  --index work/episode-index/index.json \
  --query "创始人叙事 信任" \
  --limit 6
```

`verify`must confirm the source SHA-256 and reproduce every source segment in order. Keep`index.json`, chunk Markdown/JSONL and the evidence map in`work/`; they are execution artifacts, not active knowledge entries. Lexical search is a retrieval aid, not evidence of absence. For conceptual questions, derive several transcript terms from the evidence map and search again. Exact quotations must be checked against the returned timestamped source chunk.

