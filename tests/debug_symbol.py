from src.repo_indexer import build_repo_index

index = build_repo_index(
    "pallets/flask"
)

for item in index:

    if item["file"] == "src/flask/sansio/app.py":

        print(item["functions"][:50])