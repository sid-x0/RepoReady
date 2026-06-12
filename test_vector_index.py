from vector_indexer import build_vector_index

index = build_vector_index("pallets/flask")

print("Files:", len(index))

print(index[0].keys())