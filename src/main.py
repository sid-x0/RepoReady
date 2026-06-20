from src.services import (
    summarize_repository,
    get_repository_map,
    get_start_here,
    search_repository,
    analyze_repository_issue
)

from src.vector_indexer import build_vector_index


def show_menu():

    print("\n====================")
    print("      RepoReady")
    print("====================")
    print("1. Summarize Repository")
    print("2. Repository Map")
    print("3. Start Here")
    print("4. Semantic Search")
    print("5. Analyze Issue")
    print("6. Exit")


repo_name = input(
    "Enter repository (owner/repo): "
)

print("\nBuilding repository index...")
print("This may take a minute.\n")

vector_index = build_vector_index(
    repo_name
)

print("Repository indexed successfully.")


while True:

    show_menu()

    choice = input("\nChoice: ")

    if choice == "1":

        print("\nRepo Summary")
        print("--------------------")

        result = summarize_repository(
            repo_name
        )

        print(result)

    elif choice == "2":

        print("\nRepository Map")
        print("--------------------")

        result = get_repository_map(
            repo_name
        )

        print(result)

    elif choice == "3":

        print("\nStart Here")
        print("--------------------")

        result = get_start_here(
            repo_name
        )

        for item in result:
            print(item)

    elif choice == "4":

        query = input(
            "\nSearch Query: "
        )

        results = search_repository(
            vector_index,
            query
        )

        print("\nResults")
        print("--------------------")

        for score, item in results:

            print(
                f"{round(score, 3)} | {item['file']}"
            )

    elif choice == "5":

        result = analyze_repository_issue(
            repo_name,
            vector_index
        )

        if result is None:

            print(
                "\nNo open issues found."
            )

            continue

        print("\nIssue")
        print("--------------------")

        print(
            result["issue"]["title"]
        )

        print("\nRelevant Files")
        print("--------------------")

        for score, item in result["matches"]:

            print(
                item["file"]
            )

        print("\nIssue Analysis")
        print("--------------------")

        print(
            result["explanation"]
        )

    elif choice == "6":

        print("\nGoodbye!")

        break

    else:

        print(
            "\nInvalid Choice"
        )