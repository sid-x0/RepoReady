from repo_indexer import build_repo_index_v2

index = build_repo_index_v2(
    "pallets/flask"
)

print("Indexed:", len(index))

for item in index[:5]:
    print(item["file"])
    print(item["type"])
    print()