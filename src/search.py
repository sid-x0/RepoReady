def search_symbol(index, query):
    results = []

    for item in index:

        if query in item["classes"]:
            results.append(item)

        elif query in item["functions"]:
            results.append(item)

    return results