from parser import extract_classes_functions
from github_client import get_python_files

files = get_python_files("pallets/flask")

for file in files:
    if file.path == "src/flask/app.py":
        target_file = file
        break

print(target_file.path)

content = target_file.decoded_content.decode("utf-8")

result = extract_classes_functions(content)

print(result)