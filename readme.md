# RepoReady

RepoReady is an AI-powered GitHub repository analysis tool that helps developers understand unfamiliar codebases faster.

Instead of manually reading hundreds of files, RepoReady can:

* Summarize a repository
* Explain project structure
* Identify important starting points
* Perform semantic code search
* Analyze open GitHub issues
* Suggest relevant files for contributions

---

## Features

### Repository Summary

Generate a high-level explanation of a repository directly from its README.

Example:

```text
What the project does
Main technologies used
Who would use it
Key features
```

---

### Repository Mapping

Analyze repository structure and explain the purpose of major folders.

Example:

```text
src/
tests/
docs/
.github/
```

---

### Start Here Recommendations

Highlights important files and folders for new contributors.

Examples:

```text
README.md
src/
tests/
docs/
requirements.txt
pyproject.toml
```

---

### Semantic Code Search

Search repositories using natural language instead of exact filenames.

Example queries:

```text
authentication
routing
database connection
error handling
```

RepoReady uses sentence-transformer embeddings and cosine similarity to retrieve relevant files.

---

### Issue Intelligence

Analyze GitHub issues and identify files likely related to the issue.

Example:

Issue:

```text
docs: fix typos in errorhandling.rst and views.rst
```

Output:

```text
docs/errorhandling.rst
docs/views.rst
docs/tutorial/views.rst
```

RepoReady also generates an explanation describing:

* Why files were matched
* Which files are directly referenced
* Which files are semantically related

---

## Architecture

```text
RepoReady
│
├── GitHub API Layer
│   └── github_client.py
│
├── Repository Analysis
│   ├── repo_mapper.py
│   ├── starter.py
│   └── parser.py
│
├── Embedding & Search
│   ├── embeddings.py
│   ├── vector_indexer.py
│   └── semantic_search.py
│
├── Issue Intelligence
│   └── issue_analyzer.py
│
├── LLM Layer
│   └── llm.py
│
├── Service Layer
│   └── services.py
│
└── CLI
    └── main.py
```

---

## Tech Stack

### Backend

* Python 3.10+
* PyGithub
* Tree-sitter
* Sentence Transformers
* NumPy

### AI

* Groq API
* Llama 3.3 70B Versatile
* all-MiniLM-L6-v2 embeddings

### Search

* Semantic Search
* Cosine Similarity Ranking

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/RepoReady.git
cd RepoReady
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
```

---

## Usage

Run RepoReady:

```bash
python -m src.main
```

Example:

```text
Enter repository (owner/repo): pallets/flask

1. Summarize Repository
2. Repository Map
3. Start Here
4. Semantic Search
5. Analyze Issue
6. Exit
```

---

## Current Status

### Completed

* Repository Summary
* Repository Mapping
* Start Here Recommendations
* Tree-sitter Parsing
* Repository Indexing
* Embeddings Generation
* Semantic Search
* Issue Intelligence
* Service Layer
* Interactive CLI

### Planned

* FastAPI Backend
* Persistent Vector Storage
* Web Interface
* Multi-language Support
* Repository Caching
* Dependency Graph Analysis

---

## Example Repositories Tested 

* pallets/flask
* psf/requests
* tiangolo/fastapi

---

## Motivation

Developers often spend hours understanding a new codebase before making meaningful contributions.

RepoReady aims to reduce that onboarding time by combining repository analysis, semantic search, and AI-powered explanations into a single workflow.

---

