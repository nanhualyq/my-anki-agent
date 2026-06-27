---
name: english-reading
description: Generate topic-based English reading passages at 3000-word level and add unknown words to Anki
compatibility: opencode
metadata:
  audience: learner
  vocabulary_level: 3000
---

## Overview

This skill helps you improve English reading at a 3000-word vocabulary level.

**Workflow:**
1. You request a topic — I first search the web for the latest news and information
2. Based on the search results, I generate a ~300-400 word passage at 3000-word level (ensuring timeliness)
3. You read and mark unfamiliar words/phrases
4. I add those words to your Anki deck via AnkiConnect

## Usage

### Step 1: Request a passage
I'll first search the web for the latest information on your topic, then write a passage based on real, up-to-date sources.

> "写一篇关于 [topic] 的英语文章"

### Step 2: Read and pick words
Point out the words or sentences you don't know.

### Step 3: Add to Anki
Tell me which words or sentences to add. I'll create Anki cards (Front: English word/sentence, Back: Chinese translation `<br>` grammar & vocabulary parsing notes).

## Script: add_to_anki.py

A helper script to add words to Anki via AnkiConnect.

Usage:
```bash
python3 .opencode/skills/english-reading/add_to_anki.py <deck_name> <front> <back>
```

Example:
```bash
python3 .opencode/skills/english-reading/add_to_anki.py "en-read" "abandon" "v. 放弃，遗弃"
```
