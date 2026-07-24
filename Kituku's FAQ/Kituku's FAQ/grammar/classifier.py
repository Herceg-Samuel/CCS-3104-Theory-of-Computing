"""
grammar/classifier.py
This Combines the tagger + CFG parser with a topic-to-category lookup to turn a
raw student query into a (category, confidence_source) result.

Pipeline:
    text -> tag_sequence() -> parse() -> extract_topic_words()
         -> TOPIC_KEYWORDS lookup -> category

If the CFG parse fails outright (ungrammatical / out-of-scope input), the
classifier falls back to a plain keyword search over the same
TOPIC_KEYWORDS table so the assistant can still attempt a reasonable reply
but the result is flagged source="fallback_keyword" rather than
source="grammar", which is used for evaluation/reporting in
evaluation/evaluate.py (this is the honest way to report accuracy: grammar
coverage vs. overall system coverage are reported separately).
"""

from grammar.tagger import tag_sequence
from grammar.parser import parse, extract_topic_words, extract_verbs, sentence_type

# Ordered most-specific-first: first matching keyword set wins.
TOPIC_KEYWORDS = [
    ("SPONSORSHIP_BURSARY", {"helb", "loan", "sponsorship", "sponsored", "confirmation", "waiver"}),
    ("FEE_INQUIRY", {"fee", "fees", "installment", "installments", "structure"}),
    ("EXAM_RESULTS", {"result", "results"}),
    ("TRANSCRIPT_REQUEST", {"transcript"}),
    ("ATTACHMENT_LETTER", {"attachment", "industrial", "introduction", "recommendation", "safaricom"}),
    ("RECESS_APPLICATION", {"recess"}),
    ("DEFERMENT_REQUEST", {"defer", "deferment", "deferring"}),
    ("SUPPLEMENTARY_EXAM", {"supplementary"}),
    ("UNIT_REGISTRATION", {"registration", "register", "registering", "elective", "unit", "units"}),
    ("GRADUATION_INQUIRY", {"graduation", "clearance", "ceremony"}),
    ("TIMETABLE_INQUIRY", {"timetable"}),
    ("HOSTEL_ACCOMMODATION", {"hostel", "accommodation"}),
    ("STUDENT_WELFARE", {"counselling", "welfare", "emergency", "family", "bursary", "needy"}),
    ("DISCIPLINARY_CASE", {"disciplinary"}),
    ("RESEARCH_PROJECT", {"project", "supervisor", "proposal"}),
    ("UNIT_TRANSFER", {"transfer", "transferring", "campus", "nyeri", "programme"}),
    ("APPEAL_REQUEST", {"appeal", "grade", "discontinuation"}),
    ("ID_CARD_REPLACEMENT", {"identification", "card"}),
    ("PORTAL_PASSWORD_RESET", {"password", "portal"}),
    ("GENERAL_GREETING", {"hours", "meeting", "chairman", "available"}),
]

DEFAULT_CATEGORY = "UNRECOGNISED"


def _keyword_lookup(words):
    wset = set(words)
    for category, keywords in TOPIC_KEYWORDS:
        if wset & keywords:
            return category
    return None


def classify(text: str) -> dict:
    tokens, tags = tag_sequence(text)
    tree = parse(tokens, tags)

    result = {
        "text": text,
        "tokens": tokens,
        "tags": tags,
        "grammar_ok": tree is not None,
        "sentence_type": sentence_type(tree) if tree else None,
        "topic_words": [],
        "category": DEFAULT_CATEGORY,
        "source": "none",
    }

    if tree is not None:
        topic_words = extract_topic_words(tree) + extract_verbs(tree)
        result["topic_words"] = topic_words
        category = _keyword_lookup(topic_words)
        if category:
            result["category"] = category
            result["source"] = "grammar"
            return result
        # Grammar parsed the sentence structurally but the topic wasn't
        # recognised it should still try a raw keyword fallback over the full
        # token list before giving up.

    # Fallback: raw keyword search over ALL tokens (handles ungrammatical
    # or CFG-uncovered input gracefully instead of just failing).
    category = _keyword_lookup(tokens)
    if category:
        result["category"] = category
        result["source"] = "fallback_keyword"
    return result


if __name__ == "__main__":
    tests = [
        "When is the deadline for paying second semester fees?",
        "asdkj random gibberish text unrelated to anything",
        "Can I defer my studies for one year due to financial constraints?",
    ]
    for t in tests:
        r = classify(t)
        print(t)
        print(" ->", r["category"], "| source:", r["source"],
              "| grammar_ok:", r["grammar_ok"])
