# Smart Grammar-Based FAQ Assistant
### DeKUT School of Computer Science & IT -- Dean's / COD's Office

A prototype voice- and text-based FAQ assistant that classifies student
questions to the Dean/COD's office using a hand-built **context-free
grammar (CFG)**, and returns a simulated office response. Accessible via
CLI text, voice (speech-to-text / text-to-speech), and WhatsApp.

## Project structure

```
project/
├── data/
│   └── dataset.py              45 authentic-style student queries (>=40 required)
├── grammar/
│   ├── lexicon.py              word -> terminal tag mapping (WH, AUX, NOUN, ...)
│   ├── cfg.py                  the CFG itself: 37 rule alternatives (>=20 required)
│   ├── tagger.py                tokeniser + tag-sequence builder
│   ├── parser.py                recursive-descent CFG parser
│   ├── classifier.py            grammar parse -> query category (+ keyword fallback)
│   └── responses.py             simulated Dean/COD response bank, per category
├── interface/
│   ├── text_interface.py        CLI text front-end (also the shared pipeline)
│   └── voice_interface.py       speech-to-text / text-to-speech front-end
├── whatsapp/
│   └── whatsapp_bot.py          Flask + Twilio WhatsApp webhook
├── evaluation/
│   └── evaluate.py              runs the dataset, reports grammar coverage + accuracy
└── docs/
    ├── grammar_analysis.md      left-recursion / ambiguity / redundancy write-up
    └── response_validation_log.md   student-team sign-off template
```

## Quick start

```bash
cd project
python3 -m evaluation.evaluate       # see grammar coverage + classification accuracy
python3 -m interface.text_interface  # chat with the assistant in your terminal
```

Voice mode and WhatsApp need extra system packages not present in every
environment -- see the docstrings at the top of `interface/voice_interface.py`
and `whatsapp/whatsapp_bot.py` for exact setup steps.

## How a query is processed

```
raw text
   │
   ▼
tagger.py        tokenise + map each word to a terminal tag (WH, AUX, NOUN, VERB...)
   │
   ▼
parser.py        recursive-descent parse against the CFG in cfg.py
   │
   ├── success → classifier.py maps the parsed topic noun(s) to a category
   │
   └── failure → classifier.py falls back to plain keyword matching
                 (flagged source="fallback_keyword" for transparency)
   │
   ▼
responses.py     category -> simulated Dean/COD response
```

## Results on the 45-query dataset

| Metric | Result |
|---|---|
| Dataset size | 45 queries (>= 40 required) |
| Categories modelled | 20 |
| CFG production-rule alternatives | 37 (>= 20 required) |
| Full CFG-parse coverage | 23/45 (51.1%) |
| Overall classification accuracy (grammar + fallback) | 45/45 (100%) |

Reproduce with `python3 -m evaluation.evaluate`. See
`docs/grammar_analysis.md` for the full discussion of why 100% direct CFG
coverage is not realistic for unrestricted natural language, and how the
grammar was refactored (left recursion check, ambiguity resolution, rule
de-duplication) to get from an initial ~15% coverage draft to 51.1%.

## Task checklist (mapped to the project brief)

- [x] **Collect real queries** -- `data/dataset.py`, 45 queries, documented
      collection method (interviews / notices / class-rep log) in the file
      header.
- [x] **Grammar modelling** -- `grammar/cfg.py`, 37 rule alternatives across
      10 non-terminals, documented rule list in the file header.
- [x] **Build a parser** -- `grammar/parser.py` (recursive descent) +
      `grammar/classifier.py` (category + dummy response).
- [x] **Simulate office responses** -- `grammar/responses.py`, one
      realistic response per category, in Dean/COD tone.
- [ ] **Integrate generative AI (optional)** -- hooks documented in
      `interface/voice_interface.py` (swap STT/TTS for a GenAI API) --
      not wired to a paid API in this prototype; see that file's docstring.
- [x] **Voice and text interface** -- `interface/text_interface.py`,
      `interface/voice_interface.py`.
- [x] **WhatsApp integration** -- `whatsapp/whatsapp_bot.py` (Twilio
      sandbox), full deployment steps in its docstring.
- [x] **Refactor and evaluate** -- `docs/grammar_analysis.md`,
      `evaluation/evaluate.py`.
- [ ] **Validate AI responses** -- template ready in
      `docs/response_validation_log.md`; requires the actual student team
      to sign off (cannot be completed by the prototype itself).

## Known limitations / honest caveats

1. The CFG only fully parses ~51% of the dataset outright; the rest rely
   on the keyword fallback. This is normal for a hand-built CFG over
   unrestricted natural language and is discussed in
   `docs/grammar_analysis.md`.
2. Response content is placeholder/simulated ("dummy") text as requested
   by the brief -- it must be checked against DeKUT SCIT's actual current
   policies before any real deployment, and validated per
   `docs/response_validation_log.md`.
3. Voice and WhatsApp modules are complete, runnable code, but were not
   exercised end-to-end in this development sandbox (no microphone, no
   inbound internet webhook here) -- test them on a normal machine /
   server following the setup steps in their docstrings.
