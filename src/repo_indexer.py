from src.github_client import get_repository_files
from src.parser import extract_classes_functions


def build_repo_index(repo_name):

    files = get_repository_files(repo_name)

    index = []

    for file in files:

        try:

            content = (
                file.decoded_content
                .decode("utf-8")
            )

            if file.path.endswith(".py"):

                parsed = extract_classes_functions(
                    content
                )

                index.append({
                    "file": file.path,
                    "type": "code",
                    "classes": parsed["classes"],
                    "functions": parsed["functions"],
                    "content": content[:10000]
                })

            else:

                index.append({
                    "file": file.path,
                    "type": "documentation",
                    "content": content[:10000]
                })

        except Exception:
            continue

    return index