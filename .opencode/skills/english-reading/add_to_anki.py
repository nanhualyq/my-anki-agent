import sys
import json
import urllib.request

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DEFAULT_DECK = "en-read"
DEFAULT_MODEL = "Basic"


def request(action, **params):
    body = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(ANKI_CONNECT_URL, data=body, headers={"Content-Type": "application/json"})
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python3 add_to_anki.py <front> <back> [deck_name (default: {DEFAULT_DECK})]")
        sys.exit(1)

    front = sys.argv[1]
    back = sys.argv[2]
    deck = sys.argv[3] if len(sys.argv) >= 4 else DEFAULT_DECK

    result = request("addNote", note={
        "deckName": deck,
        "modelName": DEFAULT_MODEL,
        "fields": {
            "Front": front,
            "Back": back,
        },
        "tags": [],
    })

    if result.get("error"):
        print(f"Error: {result['error']}")
        sys.exit(1)
    else:
        print(f"Added to Anki deck '{deck}': {front} -> {back}")
