"""
grammar/lexicon.py
===================
Maps surface words (from the 45-query dataset) to grammar terminal
categories ("tags"). This is the lexical layer that feeds tag sequences
into the context-free grammar defined in grammar/cfg.py.

Tag inventory (terminals of the CFG):
    WH      - question word (what, when, where, why, who, how)
    AUX     - auxiliary / copula (is, are, do, does, can, could, will, would,
              has, have)
    MODAL   - modal verb used to open a polar/imperative request (can, could,
              may, is it possible)
    HELLO   - greeting token (hello, hi)
    PRON    - pronoun (i, my, me, you, the office, we, our)
    DET     - determiner (the, a, an, my, this, next, that)
    VERB    - action verb (apply, register, pay, check, get, request, ...)
    PREP    - preposition (for, of, to, in, on, about, from, before, after)
    NOUN    - topic noun (fee, exam, results, transcript, attachment, ...)
    NEG     - negation (not, n't)
    CONJ    - conjunction (and, or)
"""

WH = {"what", "when", "where", "why", "who", "how"}

AUX = {"is", "are", "do", "does", "has", "have", "am", "was", "were"}

MODAL = {"can", "could", "will", "would", "may", "should", "must"}

HELLO = {"hello", "hi", "hey", "greetings"}

PRON = {"i", "my", "me", "you", "we", "our", "us", "myself", "it"}

DET = {"the", "a", "an", "this", "that", "next", "these", "those", "her",
       "his", "its"}

NEG = {"not", "n't", "no"}

CONJ = {"and", "or", "but"}

PREP = {"for", "of", "to", "in", "on", "about", "from", "before", "after",
        "during", "as", "at", "by", "with", "without"}

VERB = {
    "apply", "applying", "register", "registering", "pay", "paying",
    "check", "checking", "get", "getting", "request", "requesting",
    "defer", "deferring", "appeal", "appealing", "extend", "extending",
    "replace", "replacing", "transfer", "transferring", "know", "knowing",
    "obtain", "obtaining", "access", "accessing", "download", "downloading",
    "book", "booking", "schedule", "scheduling", "submit", "submitting",
    "sit", "sitting", "reset", "resetting", "issue", "issuing", "talk",
    "talking", "respond", "responding", "change", "changing", "take",
    "taking", "find", "finding", "release", "released", "come", "coming",
    "begin", "beginning", "need", "help", "available", "meet", "meeting",
    "confirm", "confirming",
}

NOUN = {
    "fee", "fees", "structure", "installments", "installment",
    "exam", "exams", "results", "result", "unit", "units", "database",
    "portal", "semester", "supplementary", "transcript", "scholarship",
    "graduation", "attachment", "introduction", "letter", "recommendation",
    "industrial", "period", "recess", "illness", "cat", "week",
    "deferment", "admission", "documents", "studies", "financial",
    "constraints", "networking", "timetable", "registration", "elective",
    "deadline", "clearance", "ceremony", "class", "hostel",
    "accommodation", "counselling", "support", "family", "emergency",
    "bursary", "needy", "students", "disciplinary", "notice",
    "decision", "department", "supervisor", "project", "proposal",
    "submission", "topic", "programme", "campus", "grade", "discontinuation",
    "university", "helb", "loan", "confirmation", "waiver",
    "government-sponsored", "government", "student", "identification",
    "card", "password", "morning", "hours", "meeting", "chairman",
    "computer", "science", "bbit", "second", "third", "final",
    "year", "safaricom", "nyeri", "main", "office", "chairman", "dean",
    "cod",
}

WORD_TAGS = {}
for w in WH: WORD_TAGS[w] = "WH"
for w in AUX: WORD_TAGS[w] = "AUX"
for w in MODAL: WORD_TAGS[w] = "MODAL"
for w in HELLO: WORD_TAGS[w] = "HELLO"
for w in PRON: WORD_TAGS[w] = "PRON"
for w in DET: WORD_TAGS[w] = "DET"
for w in NEG: WORD_TAGS[w] = "NEG"
for w in CONJ: WORD_TAGS[w] = "CONJ"
for w in PREP: WORD_TAGS[w] = "PREP"
for w in VERB: WORD_TAGS[w] = "VERB"
for w in NOUN: WORD_TAGS[w] = "NOUN"

# Words that should be ignored entirely (punctuation-like fillers)
STOPWORDS = {"please", "kindly", "there", "it", "possible"}
