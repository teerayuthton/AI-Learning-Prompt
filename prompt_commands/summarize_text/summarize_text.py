import os
from openai import OpenAI

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def summarize_text(text):
    response = client.chat.completions.create (
        model="gpt-4o-mini",
        messages=[{
            "role":"user",
            "content":f"""Summarize the text delimited by triple backticks into bullet points.
            ```{text}```"""}])
    return response.choices[0].message.content

text = "Hawaii issues volcanic toxic gas alert Thursday, May 10, 2018 - 01:43 " \
"Hawaii residents were alerted on Thursday to rising levels of toxic gas from volcanic fissures and geologists " \
"warned that Kilauea volcano may bring more fissures, lava, gas, and disaster. "

response = summarize_text(text)

print(response)