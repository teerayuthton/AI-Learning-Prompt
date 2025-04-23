import os
from openai import OpenAI
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=httpx.Client(verify=False),
)

def get_response(prompt):
    response = client.chat.completions.create (
        model="gpt-4o-mini",
        messages=[{
            "role":"user",
            "content":prompt}],
        max_tokens=100)
    return response.choices[0].message.content