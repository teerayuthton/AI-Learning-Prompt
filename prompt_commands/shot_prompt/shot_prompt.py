import os
from openai import OpenAI

import sys
sys.path.append('../')

from simple_call.simple_call import get_response

zero_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning.```
"""
print("Zero shot is: ",get_response(zero_shot_text))

one_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning. -> Bonjour
Thank you. -> ```
"""
print("One shot is: ",get_response(one_shot_text))

few_shot_text = """Translate the text delimited by triple backticks into French: ```
Good morning. -> Bonjour
Thank you. -> Merci.
How are you? -> Comment ça va?
See you later. -> ```
"""
print("Few shot is: ",get_response(few_shot_text))