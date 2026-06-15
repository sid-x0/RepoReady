from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_readme(readme_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
                
Explain this GitHub project in simple English.

Give:
1. What the project does
2. Main technologies used
3. Who would use it
4. Key features


README:
{readme_text[:6000]}
                """
            }
        ]
    )

    return response.choices[0].message.content


def explain_structure(readme, structure):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content": f"""
README:
{readme}

Structure:
{structure}

Explain what each top-level folder likely does.
Keep it concise.
"""
            }
        ]
    )
    return response.choices[0].message.content

def recommend_starting_files(readme, important_items):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
You are helping a beginner contribute to an open-source project.

README:
{readme[:4000]}

Important Files/Folders:
{important_items}

Recommend the 5 most important files/folders to read first.

For each item provide:
1. Name
2. Why it should be read
3. What the contributor will learn from it

Keep it concise.
"""
            }
        ]
    )

    return response.choices[0].message.content


def explain_issue_matches(issue, matches):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
Issue:

Title:
{issue['title']}

Body:
{issue['body']}

Relevant Files:
{matches}

Using ONLY the issue text and file names provided:

1. Explain why each file was matched.
2. Identify which files are directly mentioned.
3. Identify which files are related suggestions.
4. Do not assume any additional changes unless explicitly stated in the issue.
"""
            }
        ]
    )

    return response.choices[0].message.content