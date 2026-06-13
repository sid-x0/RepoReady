from github import Github
from dotenv import load_dotenv
from parser import extract_classes_functions
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("Github token not found")

g = Github(token)



def get_repo(repo_name):
    return g.get_repo(repo_name)

def get_readme(repo_name):
    repo = get_repo(repo_name)
    readme = repo.get_readme()
    return readme.decoded_content.decode("utf-8")

def get_python_files(repo_name):
    repo = get_repo(repo_name)

    python_files = []

    contents = repo.get_contents("")

    while contents:
        item = contents.pop(0)

        if item.type == "dir":
            contents.extend(repo.get_contents(item.path))

        elif item.path.endswith(".py"):
            python_files.append(item)

    return python_files

def get_open_issues(repo_name, limit=20):
    repo = get_repo(repo_name)

    issues = repo.get_issues(state="open")

    result = []

    for issue in issues[:limit]:
        result.append({
            "number": issue.number,
            "title": issue.title,
            "body": issue.body or "",
            "url": issue.html_url,
            "labels": [l.name for l in issue.labels]
        })

    return result