from src.vector_indexer import build_vector_index_v2

index = build_vector_index_v2(
    "pallets/flask"
)

print(len(index))

print(index[0].keys())
