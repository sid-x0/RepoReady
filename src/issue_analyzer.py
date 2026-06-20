from src.semantic_search import semantic_search
import re


def analyze_issue(issue, vector_index):

    issue_text = f"""
    {issue['title']}

    {issue['body']}
    """

    filenames = re.findall(
        r'[\w\-]+\.(?:py|rst|md|js|ts)',
        issue['title'] 
    )
    
    
    
    direct_matches = []

    for item in vector_index:

        current_filename = (
            item["file"]
            .split("/")[-1]
        )

        for target in filenames:

            if current_filename.lower() == target.lower():
                direct_matches.append(item)

    semantic_results = semantic_search(
        vector_index,
        issue_text,
        top_k=10
    )

    final_results = []
    seen = set()

    for item in direct_matches:

        final_results.append(
            (100.0, item)
        )

        seen.add(item["file"])
    

    for score, item in semantic_results:

        if item["file"] not in seen:

            final_results.append(
                (score, item)
            )

            seen.add(item["file"])

    return final_results[:5]