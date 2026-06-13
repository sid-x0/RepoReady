from github_client import get_open_issues
from vector_indexer import build_vector_index
from issue_analyzer import analyze_issue

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