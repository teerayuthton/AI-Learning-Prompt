import os
from openai import OpenAI

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def get_response(prompt):
    response = client.chat.completions.create (
        model="gpt-4o-mini",
        messages=[{
            "role":"user",
            "content":prompt}],
        max_tokens=100)
    return response.choices[0].message.content

response = get_response("How many r in strawberry")
print(response)