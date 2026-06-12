from github import Github
from dotenv import load_dotenv
from parser import extract_classes_functions
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

if not token:
    raise "Github token not found"

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

