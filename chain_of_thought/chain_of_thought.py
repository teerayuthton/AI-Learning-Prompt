import os
from openai import OpenAI

import sys
sys.path.append('../')

import simple_call

prompt = """Compute the age of my friend's father in 10 years,
given that now he's double my friend's age, and my friend is 20.
Give a step by step explanation."""

print("Chain of thought is: ",simple_call.get_response(prompt))