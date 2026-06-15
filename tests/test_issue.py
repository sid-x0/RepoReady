from src.github_client import get_open_issues
from src.vector_indexer import build_vector_index
from src.issue_analyzer import analyze_issue
from src.llm import explain_issue_matches

issues = get_open_issues("pallets/flask")

print("Issues Found:", len(issues))

issue = issues[0]

print("\nIssue:")
print(issue["title"])

index = build_vector_index("pallets/flask")

matches = analyze_issue(
    issue,
    index
)


print("\nRelevant Files:")

for score, item in matches:
    print(score, item["file"])

match_files = []

for score, item in matches:
    match_files.append({
    "file": item["file"],
    "classes": item["classes"],
    "functions": item["functions"]
    })
    
explanation = explain_issue_matches(issue, match_files)
print("\nIssue Analysis")
print("----------------------")
print(explanation)