from src.github_client import get_repository_files

files = get_repository_files(
    "pallets/flask"
)

for file in files:

    if file.path == "src/flask/app.py":

        content = (
            file.decoded_content
            .decode("utf-8")
        )

        print(
            content.find(
                "should_ignore_error"
            )
        )