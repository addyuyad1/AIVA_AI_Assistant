from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_response(prompt: str):
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content