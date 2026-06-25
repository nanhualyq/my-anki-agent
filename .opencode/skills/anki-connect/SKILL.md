---
name: anki-connect
description: Connect to Anki via AnkiConnect API, manage notes and cards
compatibility: opencode
metadata:
  audience: development
  protocol: HTTP
---

## Overview

This skill covers interacting with a local Anki desktop app via the [AnkiConnect](https://foosoft.net/projects/anki-connect/) HTTP API. AnkiConnect runs on `http://127.0.0.1:8765` by default.

All requests are `POST` to `http://127.0.0.1:8765` with a JSON body containing `action`, `version`, and `params` fields.

## Common Actions

### Health check
```json
{
  "action": "requestPermission",
  "version": 6
}
```

### Add a note
```json
{
  "action": "addNote",
  "version": 6,
  "params": {
    "note": {
      "deckName": "Default",
      "modelName": "Basic",
      "fields": {
        "Front": "question",
        "Back": "answer"
      },
      "tags": []
    }
  }
}
```

### Query cards
```json
{
  "action": "findCards",
  "version": 6,
  "params": {
    "query": "deck:Default"
  }
}
```

### Get card info
```json
{
  "action": "cardsInfo",
  "version": 6,
  "params": {
    "cards": [123]
  }
}
```

### Update note fields
```json
{
  "action": "updateNoteFields",
  "version": 6,
  "params": {
    "note": {
      "id": 123,
      "fields": {
        "Front": "updated question"
      }
    }
  }
}
```

### Delete notes
```json
{
  "action": "deleteNotes",
  "version": 6,
  "params": {
    "notes": [123]
  }
}
```

### List decks
```json
{
  "action": "deckNames",
  "version": 6
}
```

### List models (note types)
```json
{
  "action": "modelNames",
  "version": 6
}
```

## Best Practices

- Use Python's `requests` library or `curl` to interact with the API
- Always check the response for an `error` field
- Default version is `6`
- Anki must be running with AnkiConnect installed for the API to respond
- Use `curl -s -X POST http://127.0.0.1:8765 -H "Content-Type: application/json" -d '{"action": "deckNames", "version": 6}'` for quick testing
