from vector_indexer import build_vector_index
from semantic_search import semantic_search

index = build_vector_index("pallets/flask")

results = semantic_search(
    index,
    "web application"
)

for score, item in results:
    print(score)
    print(item["file"])
    print()