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