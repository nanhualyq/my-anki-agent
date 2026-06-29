---
name: anki-listen
description: Add English listening (cloze) notes to Anki's en-listen deck
compatibility: opencode
metadata:
  audience: learner
  deck: en-listen
  model: "@en-listen"
---

## Overview

This skill helps you add listening practice notes to Anki's `en-listen` deck. It uses the **`@en-listen`** note type with cloze-deleted sentences, TTS audio, Chinese translation, and pronunciation.

## Card Format

The `@en-listen` note type has 3 fields:

| Field | Content | Example |
|-------|---------|---------|
| **Text** | Cloze-deleted English sentence | `This is {{c1::a}} pen.` |
| **Back Extra** | Sentence translation `<br>` word meaning `<br>` phonemic pronunciation | `这是一支笔。<br>冠词，表示泛指<br>/ə/` |
| **Word** | Bare target word | `a` |

The card front shows the cloze sentence with TTS audio of the target word; the back reveals the full sentence, translation, word meaning, and pronunciation.

## Workflow

1. You encounter an English sentence with a word/phrase you want to learn
2. Format it as a cloze deletion (`{{c1::target_word}}`)
3. I add it to the `en-listen` deck with translation, meaning, and pronunciation

## Usage

> "把这句话加入听力：'This is a pen.'，生词是 'a'，翻译是 '这是一支笔。'，含义是 '冠词，表示泛指'，发音是 /ə/"

I'll create an Anki card in the `en-listen` deck with:
- **Text:** `This is {{c1::a}} pen.`
- **Back Extra:** `这是一支笔。<br>冠词，表示泛指<br>/ə/`
- **Word:** `a`

## Script: add_to_anki.py

A helper script to add listening notes to Anki via AnkiConnect.

```bash
python3 .opencode/skills/anki-listen/add_to_anki.py <sentence> <word> <translation> <meaning> <pronunciation>
```

Example:
```bash
python3 .opencode/skills/anki-listen/add_to_anki.py "This is a pen." "a" "这是一支笔。" "冠词，表示泛指" "/ə/"
```
