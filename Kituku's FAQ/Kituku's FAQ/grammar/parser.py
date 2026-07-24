"""
grammar/parser.py
==================
A small backtracking recursive-descent parser for the CFG defined in
grammar/cfg.py. It parses a TAG sequence (not raw words) top-down from the
start symbol S, and succeeds only if the *entire* tag sequence is consumed
(full-sentence coverage).

Ambiguity handling: alternatives for a non-terminal are tried in the order
given in GRAMMAR (longest / most specific alternative first -- see
cfg.py header notes), and the parser returns the FIRST successful full
derivation. This gives deterministic, reproducible parses.
"""

from grammar.cfg import GRAMMAR, START_SYMBOL, TERMINALS


class ParseNode:
    def __init__(self, symbol, children=None, word=None):
        self.symbol = symbol
        self.children = children or []
        self.word = word  # only set for terminal leaves

    def leaves(self):
        if self.word is not None:
            return [(self.symbol, self.word)]
        out = []
        for c in self.children:
            out.extend(c.leaves())
        return out

    def pretty(self, indent=0):
        pad = "  " * indent
        if self.word is not None:
            return f"{pad}{self.symbol} -> '{self.word}'"
        lines = [f"{pad}{self.symbol}"]
        for c in self.children:
            lines.append(c.pretty(indent + 1))
        return "\n".join(lines)


def _match_symbol(symbol, tokens, tags, pos):
    """Try to match a single grammar symbol at position `pos`.
    Returns (node, new_pos) or (None, pos) on failure."""
    if symbol in TERMINALS:
        if pos < len(tags) and tags[pos] == symbol:
            node = ParseNode(symbol, word=tokens[pos])
            return node, pos + 1
        return None, pos

    # non-terminal: try each alternative (already ordered longest-first)
    for alternative in GRAMMAR[symbol]:
        children = []
        cur = pos
        ok = True
        for sub_symbol in alternative:
            child, cur = _match_symbol(sub_symbol, tokens, tags, cur)
            if child is None:
                ok = False
                break
            children.append(child)
        if ok:
            return ParseNode(symbol, children=children), cur
    return None, pos


def parse(tokens, tags):
    """Attempt a full parse of the tag sequence. Returns a ParseNode or
    None if no rule sequence covers the entire input."""
    node, end_pos = _match_symbol(START_SYMBOL, tokens, tags, 0)
    if node is not None and end_pos == len(tags):
        return node
    return None


def extract_topic_words(node: ParseNode):
    """Pull out the surface NOUN words from a successful parse -- these
    are used downstream to map the parse onto a query category."""
    if node is None:
        return []
    return [word for (sym, word) in node.leaves() if sym == "NOUN"]


def extract_verbs(node: ParseNode):
    if node is None:
        return []
    return [word for (sym, word) in node.leaves() if sym == "VERB"]


def sentence_type(node: ParseNode):
    """Top-level rule matched: WHQ / POLARQ / IMPQ / GREETING."""
    if node is None or not node.children:
        return None
    return node.children[0].symbol


if __name__ == "__main__":
    from grammar.tagger import tag_sequence

    tests = [
        "When is the deadline for paying second semester fees?",
        "Can I defer my studies for one year due to financial constraints?",
        "Hello, what are the Dean's office hours this week?",
        "How do I register for my third year units on the student portal?",
    ]
    for t in tests:
        toks, tags = tag_sequence(t)
        tree = parse(toks, tags)
        print("Q:", t)
        print(" tags:", tags)
        if tree:
            print(" parse OK  | type:", sentence_type(tree),
                  "| topic words:", extract_topic_words(tree))
        else:
            print(" parse FAILED")
        print()
