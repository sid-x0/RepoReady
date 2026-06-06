from github import Github
from dotenv import load_dotenv
from llm import summarize_readme
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

if not token:
    print("GitHub token not found!")
    exit()

g = Github(token)

repo = g.get_repo("microsoft/vscode")

print("Name:", repo.name)
print("Description:", repo.description)
print("Stars:", repo.stargazers_count)

content = repo.get_readme().decoded_content.decode("utf-8")

summary = summarize_readme(content)

print(summary)