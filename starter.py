def find_important_items(structure):
    important_keywords = [
        "README",
        "src",
        "app",
        "core",
        "backend",
        "frontend",
        "api",
        "tests",
        "docs",
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "setup.py",
        "Dockerfile"
    ]

    important = []

    for line in structure.split("\n"):
        for keyword in important_keywords:
            if keyword.lower() in line.lower():
                important.append(line)
                break

    return important