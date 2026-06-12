from repo_indexer import build_repo_index
from search import search_symbol

index = build_repo_index("pallets/flask")

results = search_symbol(index, "Config")

for result in results:
    print(result)