from repo_indexer import build_repo_index

index = build_repo_index("pallets/flask")

print("Files Parsed:", len(index))

for item in index[:5]:
    print(item)