import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

# Define the conversation
conversation =[
    {"role": "system",
    "content":"You are a travel guide designed to provide information about landmarks that tourists should explore in Paris. You speak in a concise manner."},
    {"role":"user",
    "content":"What is the most famous landmark in Paris?"},
    {"role":"assistant",
    "content":"The most famous landmark in Paris is the Eiffel Tower."},
]

# Define a list of questions
questions = [
    "How far away is the Louvre from the Eiffel Tower (in driving miles)?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

for question in questions:

    input_dict = {"role": "user", "content":question}

    conversation.append(input_dict)

    # Make the next API call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

    # Print the response from the model
    resp = response.choices[0].message.content
    print(resp)
