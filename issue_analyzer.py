from semantic_search import semantic_search


def analyze_issue(issue, vector_index):

    query = f"""
    {issue['title']}

    {issue['body']}
    """

    matches = semantic_search(
        vector_index,
        query,
        top_k=5
    )

    return matches