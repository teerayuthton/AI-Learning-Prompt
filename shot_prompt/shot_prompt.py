import os
from openai import OpenAI

import sys
sys.path.append('../')

import simple_call

zero_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning.```
"""
print("Zero shot is: ",simple_call.get_response(zero_shot_text))

one_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning. -> Bonjour
Thank you. -> ```
"""
print("One shot is: ",simple_call.get_response(one_shot_text))

few_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning. -> Bonjour
Thank you. -> Merci.
How are you? -> Comment ça va?
See you later. -> ```
"""
print("Few shot is: ",simple_call.get_response(few_shot_text))