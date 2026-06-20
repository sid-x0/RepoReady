from src.github_client import (
    get_readme,
    get_open_issues
)

from src.llm import (
    summarize_readme,
    explain_structure,
    explain_issue_matches
)

from src.repo_mapper import get_repo_structure
from src.starter import find_important_items
from src.vector_indexer import build_vector_index
from src.semantic_search import semantic_search
from src.issue_analyzer import analyze_issue


def summarize_repository(repo_name):

    readme = get_readme(repo_name)

    summary = summarize_readme(
        readme
    )

    return summary


def get_repository_map(repo_name):

    readme = get_readme(repo_name)

    structure = get_repo_structure(
        repo_name
    )

    explanation = explain_structure(
        readme,
        structure
    )

    return explanation

def get_start_here(repo_name):

    structure = get_repo_structure(
        repo_name
    )

    important = find_important_items(
        structure
    )

    return important


def search_repository(
    vector_index,
    query
):


    results = semantic_search(
        vector_index,
        query
    )

    return results

def analyze_repository_issue(
    repo_name,
    vector_index
):

    issues = get_open_issues(repo_name)

    if not issues:
        return None

    issue = issues[0]

    matches = analyze_issue(
        issue,
        vector_index
    )

    match_files = []

    for score, item in matches:

        match_files.append({
            "file": item["file"],
            "type": item["type"]
        })

    explanation = explain_issue_matches(
        issue,
        match_files
    )

    return {
        "issue": issue,
        "matches": matches,
        "explanation": explanation
    }