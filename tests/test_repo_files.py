from src.github_client import get_repository_files

files = get_repository_files(
    "pallets/flask"
)

print("Files:", len(files))

for file in files[:20]:
    print(file.path)
    