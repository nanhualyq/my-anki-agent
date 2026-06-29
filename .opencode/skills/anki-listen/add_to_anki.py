import sys
import json
import urllib.request

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DEFAULT_DECK = "en-listen"
DEFAULT_MODEL = "@en-listen"


def request(action, **params):
    body = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(ANKI_CONNECT_URL, data=body, headers={"Content-Type": "application/json"})
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())


def make_cloze(sentence, word):
    import re
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    match = pattern.search(sentence)
    if match:
        start, end = match.start(), match.end()
        return sentence[:start] + "{{c1::" + sentence[start:end] + "}}" + sentence[end:]
    return sentence


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(f"Usage: python3 {sys.argv[0]} <sentence> <word> <translation> <meaning> <pronunciation> [deck_name]")
        sys.exit(1)

    sentence = sys.argv[1]
    word = sys.argv[2]
    translation = sys.argv[3]
    meaning = sys.argv[4]
    pronunciation = sys.argv[5]
    deck = sys.argv[6] if len(sys.argv) >= 7 else DEFAULT_DECK

    cloze_text = make_cloze(sentence, word)
    back_extra = f"{translation}<br>{meaning}<br>{pronunciation}"

    result = request("addNote", note={
        "deckName": deck,
        "modelName": DEFAULT_MODEL,
        "fields": {
            "Text": cloze_text,
            "Back Extra": back_extra,
            "Word": word,
        },
        "tags": [],
    })

    if result.get("error"):
        print(f"Error: {result['error']}")
        sys.exit(1)
    else:
        print(f"Added to Anki deck '{deck}': {sentence} (word: {word})")
