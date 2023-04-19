'''
open ai api test
'''

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('openai')

# Set the model and prompt
model_engine = "text-davinci-003"
with open(os.path.splitext(__file__)[0]) as file:
    all = file.read().splitlines()
    last = all[-1]

print(1, last)
max_tokens = 1024

completion = openai.Completion.create(
    engine=model_engine,
    prompt=last,
    max_tokens=max_tokens,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(completion.choices[0].text)
