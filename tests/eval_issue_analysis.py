from src.vector_indexer import build_vector_index
from src.issue_analyzer import analyze_issue

from tests.eval_dataset import EVAL_CASES


top1_hits = 0
top3_hits = 0
top5_hits = 0

total_cases = len(EVAL_CASES)


for case in EVAL_CASES:

    print("\n" + "=" * 60)

    print("Issue:")
    print(case["issue"]["title"])

    print("=" * 60)

    index = build_vector_index(
        case["repo"]
    )

    matches = analyze_issue(
        case["issue"],
        index
    )

    predicted = [
        item["file"]
        for score, item in matches
    ]

    expected = case["expected"]

    top1 = any(
        file in predicted[:1]
        for file in expected
    )

    top3 = any(
        file in predicted[:3]
        for file in expected
    )

    top5 = any(
        file in predicted[:5]
        for file in expected
    )

    if top1:
        top1_hits += 1

    if top3:
        top3_hits += 1

    if top5:
        top5_hits += 1

    print("\nTop 5 Retrieved Files:")

    for i, file in enumerate(predicted, start=1):
        print(f"{i}. {file}")

    print("\nExpected Files:")

    for file in expected:
        print(file)

    print("\nResults:")
    print("Top-1:", top1)
    print("Top-3:", top3)
    print("Top-5:", top5)

    print()


print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)

print(
    f"Top-1 Accuracy: {(top1_hits / total_cases) * 100:.2f}%"
)

print(
    f"Top-3 Accuracy: {(top3_hits / total_cases) * 100:.2f}%"
)

print(
    f"Top-5 Accuracy: {(top5_hits / total_cases) * 100:.2f}%"
)