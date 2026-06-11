from github_client import get_repo, get_readme
from llm import summarize_readme


repo_name = input("Enter repository (owner/repo): ")

repo = get_repo(repo_name)

print("\nRepository Information")
print("----------------------")
print("Name:", repo.name)
print("Description:", repo.description)
print("Stars:", repo.stargazers_count)

print("\nFetching README...\n")

content = get_readme(repo_name)

summary = summarize_readme(content)

print("\nRepoReady Summary")
print("----------------------")
print(summary)