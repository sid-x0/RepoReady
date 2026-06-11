from github import Github
from dotenv import load_dotenv
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