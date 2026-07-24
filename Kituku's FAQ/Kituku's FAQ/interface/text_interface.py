"""
interface/text_interface.py

Text-based command-line interface for the Smart Grammar-Based FAQ
Assistant. This is the reference implementation of the "text input/output"
half of the brief's accessibility requirement, and is what
whatsapp/whatsapp_bot.py and interface/voice_interface.py both call into.

Run with:  python3 -m interface.text_interface
"""

from grammar.classifier import classify
from grammar.responses import get_response

WELCOME = """
========================================================================
 DeKUT School of Computer Science & IT FAQ Assistant (prototype)
 Ask a question the way you would ask the Dean's or COD's office.
 Type 'exit' to quit.
========================================================================
"""


def handle_query(text: str, addressee: str = "Dean/COD") -> dict:
    """Single entry point reused by text, voice and WhatsApp front-ends."""
    result = classify(text)
    reply = get_response(result["category"], addressee=addressee)
    result["reply"] = reply
    return result


def run_cli():
    print(WELCOME)
    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not text:
            continue
        if text.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        result = handle_query(text)
        print(f"[category: {result['category']}  |  "
              f"parsed_by: {result['source']}]")
        print(f"Assistant: {result['reply']}\n")


if __name__ == "__main__":
    run_cli()
