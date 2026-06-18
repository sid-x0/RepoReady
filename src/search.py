def search_symbol(index, query):

    results = []

    query = query.lower()

    for item in index:

        classes = item.get("classes", [])
        functions = item.get("functions", [])

        if any(query in cls.lower() for cls in classes):
            results.append(item)

        elif any(query in func.lower() for func in functions):
            results.append(item)

    return results