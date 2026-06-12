from github_client import get_repo

def get_repo_structure(repo_name):
    repo = get_repo(repo_name)

    contents = repo.get_contents("")

    structure = []

    for item in contents:
        structure.append(f"{item.path} ({item.type})")

    return "\n".join(structure)