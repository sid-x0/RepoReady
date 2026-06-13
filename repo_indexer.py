from github_client import get_python_files
from parser import extract_classes_functions


def build_repo_index(repo_name):
    files = get_python_files(repo_name)

    index = []
    
    SKIP_FOLDERS = [
    "tests/",
    "docs/",
    "examples/"
    ]

    for file in files:
        try:
            content = file.decoded_content.decode("utf-8")

            # Skip files in skip folders
            if any(folder in file.path for folder in SKIP_FOLDERS):
                continue

            parsed = extract_classes_functions(content)

            index.append({
                "file": file.path,
                "classes": parsed["classes"],
                "functions": parsed["functions"],
                "content": content[:2000]
            })

        except Exception:
            continue

    return index