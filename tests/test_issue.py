from src.services import analyze_repository_issue

result = analyze_repository_issue(
    "pallets/flask"
)

print(result["issue"]["title"])

for score, item in result["matches"]:
    print(score, item["file"])

print(result["explanation"])