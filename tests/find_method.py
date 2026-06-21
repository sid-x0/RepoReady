# tests/find_method.py

from src.github_client import get_repository_files

files = get_repository_files("pallets/flask")

for file in files:

    if file.path == "src/flask/sansio/app.py":

        content = (
            file.decoded_content
            .decode("utf-8")
        )

        lines = content.splitlines()

        for i, line in enumerate(lines):

            if "should_ignore_error" in line:

                print(
                    f"Found at line {i+1}:"
                )

                print(line)