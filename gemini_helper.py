import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_roadmap(role):

    prompt=f"""
Create a roadmap for becoming a {role}

Return ONLY:

Skill|Timeline|Project|Resource

Example:

Python|Month 1|Calculator App|Python Docs
DSA|Month 2|Sorting Visualizer|Neetcode

No headings
No explanations
"""

    response=model.generate_content(
        prompt
    )

    return response.text