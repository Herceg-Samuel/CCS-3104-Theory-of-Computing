"""
evaluation/evaluate.py

Runs the entire 45-query dataset through the grammar/classifier pipeline
and reports:
  1. Grammar coverage: % of queries the CFG parser fully derives.
  2. Classification accuracy: % of queries assigned the correct gold
     category (via grammar OR keyword fallback).
  3. Per-category breakdown and a confusion list of misclassifications.

Run with:  python3 -m evaluation.evaluate from root folder
"""

from data.dataset import QUERIES
from grammar.classifier import classify


def run_evaluation(verbose=True):
    total = len(QUERIES)
    grammar_ok_count = 0
    correct_count = 0
    correct_via_grammar = 0
    misclassified = []

    for q in QUERIES:
        result = classify(q["text"])
        if result["grammar_ok"]:
            grammar_ok_count += 1
        is_correct = result["category"] == q["category"]
        if is_correct:
            correct_count += 1
            if result["source"] == "grammar":
                correct_via_grammar += 1
        else:
            misclassified.append((q, result))

    grammar_coverage = grammar_ok_count / total * 100
    accuracy = correct_count / total * 100

    if verbose:
        print("=" * 70)
        print(f"FAQ ASSISTANT. GRAMMAR & CLASSIFIER EVALUATION")
        print("=" * 70)
        print(f"Dataset size                         : {total} queries")
        print(f"CFG full-parse coverage               : {grammar_ok_count}/{total} "
              f"({grammar_coverage:.1f}%)")
        print(f"Overall classification accuracy       : {correct_count}/{total} "
              f"({accuracy:.1f}%)")
        print(f"  ...of which correctly classified via grammar (not fallback): "
              f"{correct_via_grammar}/{total} ({correct_via_grammar/total*100:.1f}%)")
        print()
        if misclassified:
            print(f"Misclassified queries ({len(misclassified)}):")
            for q, r in misclassified:
                print(f"  [{q['id']:>2}] \"{q['text']}\"")
                print(f"        expected={q['category']:<22} got={r['category']:<22} "
                      f"source={r['source']} grammar_ok={r['grammar_ok']}")
        else:
            print("No misclassifications. ")
        print("=" * 70)

    return {
        "total": total,
        "grammar_coverage_pct": grammar_coverage,
        "accuracy_pct": accuracy,
        "misclassified": misclassified,
    }


if __name__ == "__main__":
    run_evaluation()
