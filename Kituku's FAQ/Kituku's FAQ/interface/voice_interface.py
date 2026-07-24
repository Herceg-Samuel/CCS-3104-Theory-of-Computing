"""
interface/voice_interface.py

Voice front-end for the FAQ assistant: speech-to-text (STT) input and
text-to-speech (TTS) output, wired into the same handle_query() pipeline
used by the text interface and the WhatsApp bot.

NOTE ON DEPLOYMENT ENVIRONMENT:
This module needs a microphone and audio output device. run it with:

    pip install SpeechRecognition pyttsx3 pyaudio
    python3 -m interface.voice_interface

On Linux you may need to run: sudo apt-get install portaudio19-dev espeak
in order to get the audio libraries needed by pyaudio and pyttsx3.

Two backends are supported for STT:
  * "google"  - speech_recognition's built-in free Google Web Speech API
                (needs internet, no API key, good for prototyping/demo).
  * "sphinx"  - CMU PocketSphinx, fully offline (lower accuracy).

"""

import sys

from interface.text_interface import handle_query

STT_BACKEND = "google"  


def _lazy_imports():
    """speech_recognition / pyttsx3 need system audio libraries that may
    not be installed in every environment -- import lazily with a clear
    error message instead of crashing the whole package on import."""
    try:
        import speech_recognition as sr
    except ImportError:
        print("Missing dependency: pip install SpeechRecognition pyaudio")
        sys.exit(1)
    try:
        import pyttsx3
    except ImportError:
        print("Missing dependency: pip install pyttsx3")
        sys.exit(1)
    return sr, pyttsx3


def listen(recognizer, microphone, sr_module) -> str:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        if STT_BACKEND == "sphinx":
            return recognizer.recognize_sphinx(audio)
        return recognizer.recognize_google(audio)
    except sr_module.UnknownValueError:
        return ""
    except sr_module.RequestError as e:
        print(f"STT service error: {e}")
        return ""


def speak(engine, text: str):
    engine.say(text)
    engine.runAndWait()


def run_voice_loop():
    sr, pyttsx3 = _lazy_imports()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    print("Smart FAQ Assistant -- voice mode. Say 'exit' to quit.")
    speak(engine, "Hello. How can the Dean or Chair of Department help you today?")

    while True:
        text = listen(recognizer, microphone, sr)
        if not text:
            print("(didn't catch that, please try again)")
            continue
        print("You said:", text)
        if text.strip().lower() in {"exit", "quit", "stop"}:
            speak(engine, "Goodbye.")
            break

        result = handle_query(text)
        print(f"[category: {result['category']} | source: {result['source']}]")
        print("Assistant:", result["reply"])
        speak(engine, result["reply"])


if __name__ == "__main__":
    run_voice_loop()
