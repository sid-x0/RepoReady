from src.services import (
    summarize_repository,
    get_repository_map,
    get_start_here,
    search_repository
)

repo = "pallets/flask"

print(summarize_repository(repo))

print(get_repository_map(repo))

print(get_start_here(repo))

results = search_repository(
    repo,
    "routing"
)

for score, item in results:
    print(score, item["file"])