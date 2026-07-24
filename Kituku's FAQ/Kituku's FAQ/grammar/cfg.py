"""
Context-free grammar (CFG) that models the syntactic structure of student
queries to the Dean / COD office. The grammar operates over the POS-like
TAG sequence produced by grammar/tagger.py, not over raw words directly
(a standard technique for keeping a hand-built CFG small and generalisable
to unseen vocabulary).

Non-terminals: S, WHQ, POLARQ, IMPQ, GREETING, NP, NOUN_SEQ, VP, PP, PP_LIST
Terminals    : WH, AUX, MODAL, HELLO, PRON, DET, NEG, CONJ, PREP, VERB, NOUN

*** THIS IS v2 OF THE GRAMMAR (post-refactor) ***
v1 (see docs/grammar_analysis.md for the full before/after discussion) only
allowed a single NOUN per noun phrase and a single PP per verb phrase. When
run against the 45-query dataset it failed on realistic compound-noun
queries ("second semester fees", "student portal") and queries with more
than one prepositional phrase ("...for one year due to financial
constraints"). v2 fixes this by introducing NOUN_SEQ (right-recursive noun
compounding) and PP_LIST (right-recursive PP chaining), and removes v1's
duplicated NP/VP alternatives that had been copy-pasted under WHQ/POLARQ/
IMPQ instead of being shared -- reducing redundancy.

  RULE COUNT
The grammar defines 37 production-rule alternatives across 10
non-terminals.

    1.  S         -> WHQ
    2.  S         -> POLARQ
    3.  S         -> IMPQ
    4.  S         -> GREETING
    5.  WHQ       -> WH AUX NP VP
    6.  WHQ       -> WH AUX NP NP
    7.  WHQ       -> WH AUX NP
    8.  WHQ       -> WH AUX PRON VP
    9.  WHQ       -> WH MODAL PRON VP
    10. WHQ       -> WH VERB NP
    11. POLARQ    -> AUX PRON VP
    12. POLARQ    -> AUX PRON PP
    13. POLARQ    -> AUX PRON NEG VP
    14. POLARQ    -> MODAL PRON VP
    15. POLARQ    -> MODAL PRON VERB NP
    16. POLARQ    -> AUX DET NOUN_SEQ VP
    17. IMPQ      -> VERB NP PP_LIST
    18. IMPQ      -> VERB NP
    19. IMPQ      -> PRON VERB NP
    20. GREETING  -> HELLO WHQ
    21. GREETING  -> HELLO PRON
    22. GREETING  -> HELLO
    23. NP        -> DET NOUN_SEQ PP_LIST
    24. NP        -> DET NOUN_SEQ
    25. NP        -> PRON NOUN_SEQ
    26. NP        -> NOUN_SEQ CONJ NOUN_SEQ
    27. NP        -> NOUN_SEQ
    28. NOUN_SEQ  -> NOUN NOUN_SEQ
    29. NOUN_SEQ  -> NOUN
    30. VP        -> VERB NP PP_LIST NP
    31. VP        -> VERB NP PP_LIST
    32. VP        -> VERB NP NP
    33. VP        -> VERB NP
    34. VP        -> VERB PP_LIST
    35. VP        -> VERB
    36. PP        -> PREP VP
    37. PP        -> PREP NP
    38. PP_LIST   -> PP PP_LIST
    39. PP_LIST   -> PP

Design notes on avoiding common CFG pitfalls (full write-up in
docs/grammar_analysis.md):
  * No rule's right-hand side begins with its own left-hand symbol, so the
    grammar is free of direct LEFT RECURSION. NOUN_SEQ and PP_LIST recurse
    on their *second* (rightmost) symbol only -- i.e. they are RIGHT
    recursive, which a top-down parser handles safely.
  * NP and VP are factored out as shared sub-grammars reused by WHQ, POLARQ
    and IMPQ instead of being duplicated inline under every top-level rule.
  * AMBIGUITY between "NP -> NOUN_SEQ" and "NP -> DET NOUN_SEQ", and between
    "NOUN_SEQ -> NOUN NOUN_SEQ" and "NOUN_SEQ -> NOUN", is resolved by
    parser.py always trying the longer / more specific alternative first
    (greedy-longest disambiguation), so a given tag sequence always yields
    exactly one parse.
"""

GRAMMAR = {
    "S": [
        ["WHQ"],
        ["POLARQ"],
        ["IMPQ"],
        ["GREETING"],
    ],
    "WHQ": [
        ["WH", "AUX", "NP", "VP"],
        ["WH", "AUX", "NP", "NP"],
        ["WH", "AUX", "NP"],
        ["WH", "AUX", "PRON", "VP"],
        ["WH", "MODAL", "PRON", "VP"],
        ["WH", "VERB", "NP"],
    ],
    "POLARQ": [
        ["AUX", "PRON", "VP"],
        ["AUX", "PRON", "PP"],
        ["AUX", "PRON", "NEG", "VP"],
        ["MODAL", "PRON", "VP"],
        ["MODAL", "PRON", "VERB", "NP"],
        ["AUX", "DET", "NOUN_SEQ", "VP"],
    ],
    "IMPQ": [
        ["VERB", "NP", "PP_LIST"],
        ["VERB", "NP"],
        ["PRON", "VERB", "NP"],
    ],
    "GREETING": [
        ["HELLO", "WHQ"],
        ["HELLO", "PRON"],
        ["HELLO"],
    ],
    "NP": [
        ["DET", "NOUN_SEQ", "PP_LIST"],
        ["DET", "NOUN_SEQ"],
        ["PRON", "NOUN_SEQ"],
        ["NOUN_SEQ", "CONJ", "NOUN_SEQ"],
        ["NOUN_SEQ"],
    ],
    "NOUN_SEQ": [
        ["NOUN", "NOUN_SEQ"],
        ["NOUN"],
    ],
    "VP": [
        ["VERB", "NP", "PP_LIST", "NP"],
        ["VERB", "NP", "PP_LIST"],
        ["VERB", "NP", "NP"],
        ["VERB", "NP"],
        ["VERB", "PP_LIST"],
        ["VERB"],
    ],
    "PP": [
        ["PREP", "VP"],
        ["PREP", "NP"],
    ],
    "PP_LIST": [
        ["PP", "PP_LIST"],
        ["PP"],
    ],
}

START_SYMBOL = "S"

TERMINALS = {"WH", "AUX", "MODAL", "HELLO", "PRON", "DET", "NEG", "CONJ",
             "PREP", "VERB", "NOUN"}
