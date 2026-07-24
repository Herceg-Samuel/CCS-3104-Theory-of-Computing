"""
grammar/tagger.py

Tokenises and tags a raw student query into the terminal-tag sequence
consumed by the CFG in grammar/cfg.py.

Unknown-word handling (documented so the grammar
generalises beyond the exact 45-query training set):
  - A capitalised-looking / unseen word ending in typical noun morphology,
    or simply any unseen content word, defaults to NOUN (treated as a topic
    word) this lets the parser cope with campus/unit names not
    present in the lexicon (e.g. "Safaricom", "BBIT").
  - Unseen words matching a small verb-suffix heuristic default to VERB.
  - Everything else unseen is dropped (treated as a filler/stopword) so it
    does not break the parse.
"""

import re
from grammar.lexicon import WORD_TAGS, STOPWORDS

_VERB_SUFFIXES = ("ing", "ed")
_WORD_RE = re.compile(r"[A-Za-z']+")


def tokenize(text: str):
    return _WORD_RE.findall(text.lower())


def tag_token(token: str) -> str:
    if token in WORD_TAGS:
        return WORD_TAGS[token]
    if token in STOPWORDS:
        return None
    if token.endswith(_VERB_SUFFIXES):
        return "VERB"
    # default: unseen content word treated as a topic NOUN
    return "NOUN"


def tag_sequence(text: str):
    """Return (tokens, tags) with stopwords/filler tokens removed."""
    tokens = tokenize(text)
    tokens_out, tags_out = [], []
    for tok in tokens:
        tag = tag_token(tok)
        if tag is None:
            continue
        tokens_out.append(tok)
        tags_out.append(tag)
    return tokens_out, tags_out


if __name__ == "__main__":
    samples = [
        "When is the deadline for paying second semester fees?",
        "Can I defer my studies for one year due to financial constraints?",
        "Hello, what are the Dean's office hours this week?",
    ]
    for s in samples:
        toks, tags = tag_sequence(s)
        print(s)
        print(" ", list(zip(toks, tags)))
