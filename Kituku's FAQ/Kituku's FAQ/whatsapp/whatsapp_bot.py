"""
whatsapp/whatsapp_bot.py

WhatsApp integration for the FAQ assistant using Twilio's WhatsApp Business
API (the standard, fastest way for a student project to get a real
WhatsApp number talking to Python -- no Meta Business verification needed
for the Twilio Sandbox during development/demo).

DEPLOYMENT STEPS (documented here since this sandbox cannot reach
api.twilio.com or receive inbound webhooks itself):
  1. Create a free Twilio account on: https://www.twilio.com/whatsapp
  2. In Console -> Messaging -> Try it out -> Send a WhatsApp message,
     join the sandbox (send the given code to the given number from your
     phone).
  3. `pip install flask twilio`
  4. Run this file: `python3 whatsapp_bot.py` (starts Flask on :5000).
  5. Expose it publicly for Twilio's webhook, e.g. with ngrok:
         ngrok http 5000
  6. In the Twilio Console, set the Sandbox's "WHEN A MESSAGE COMES IN"
     webhook URL to  https://<your-ngrok-id>.ngrok.io/whatsapp
  7. Message the Twilio sandbox number from WhatsApp -- replies come from
     handle_query() in interface/text_interface.py, so text and WhatsApp
     always classify identically.

For a production (non-sandbox) deployment, apply for a WhatsApp Business
Profile via Twilio (or Meta Cloud API directly) and point the same webhook
at your production URL -- no other code changes needed.
"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from interface.text_interface import handle_query

app = Flask(__name__)


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_text = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "unknown")

    result = handle_query(incoming_text)
    reply_text = result["reply"]

    # Prefix with the matched category for transparency during the demo /
    # student-team validation phase. Remove this prefix for the final
    # production deployment if a cleaner student-facing reply is wanted.
    debug_prefix = f"[{result['category']}]\n"
    full_reply = debug_prefix + reply_text

    print(f"WhatsApp message from {from_number}: {incoming_text!r} "
          f"-> category={result['category']} source={result['source']}")

    twiml = MessagingResponse()
    twiml.message(full_reply)
    return str(twiml)


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
