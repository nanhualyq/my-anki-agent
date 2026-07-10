---
name: english-reading
description: Generate topic-based English reading passages at 4000-word level and add unknown words to Anki
compatibility: opencode
metadata:
  audience: learner
  vocabulary_level: 4000
---

## Overview

This skill helps you improve English reading at a 4000-word vocabulary level.

## Defaults

- **Deck:** `en-read`
- **Note Type:** `Basic` (Front / Back)

## Card Format

Cards use the **Basic** note type with:
- **Front:** English word, phrase, or sentence
- **Back:** Chinese translation `<br>` grammar & vocabulary parsing notes

The `<br>` tag separates the translation from the parsing notes so they display on separate lines in Anki.

## Workflow

1. You request a topic — I first search the web for the latest news and information
2. Based on the search results, I generate a ~300-400 word passage at 4000-word level (ensuring timeliness)
3. You read and mark unfamiliar words/phrases
4. I add those words to your Anki deck via AnkiConnect

## Usage

### Step 1: Request a passage
I'll first search the web for the latest information on your topic, then write a passage based on real, up-to-date sources and save it to a `.md` file so you can easily open it and bold unfamiliar words.

> "写一篇关于 [topic] 的英语文章"

### Step 2: Read and pick words
Point out the words or sentences you don't know.

### Step 3: Add to Anki
Tell me which words or sentences to add. I'll create Anki cards (`en-read` deck, `Basic` note type).

- **Front:** English word/sentence
- **Back:** Chinese translation `<br>` grammar & vocabulary parsing notes

## Script: add_to_anki.py

A helper script to add words to Anki via AnkiConnect. Deck defaults to `en-read`, note type to `Basic`.

Usage:
```bash
python3 .opencode/skills/english-reading/add_to_anki.py <front> <back> [deck_name]
```

Examples:
```bash
python3 .opencode/skills/english-reading/add_to_anki.py "abandon" "v. 放弃，遗弃<br>abandon = 放弃，常指彻底放弃"
python3 .opencode/skills/english-reading/add_to_anki.py "hello" "你好" "en-listen"
```
