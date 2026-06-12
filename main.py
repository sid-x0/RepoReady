from github_client import get_repo, get_readme
from llm import summarize_readme, explain_structure, recommend_starting_files
from repo_mapper import get_repo_structure 
from starter import find_important_items


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

structure = get_repo_structure(repo_name)

print("\nRepo structure")
print("----------------------")
print(explain_structure(content, structure))

important_items = find_important_items(structure)

start_here = recommend_starting_files(
    content,
    "\n".join(important_items)
)

print("\nSTART HERE")
print("----------------------")
print(start_here)


