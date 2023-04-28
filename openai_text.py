'''
open ai api
'''

from dotenv import load_dotenv
import openai
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv('openai')


def main():
    st.write('Welcome to')
    user_input = st.text_input("Describe your LinkedIn post: ")
    if st.button('generate post'):
        st.write(get_answer(user_input))


def get_answer(post):
    '''Set the model and prompt'''

    model_engine = "text-davinci-003"
    # with open(os.path.splitext(__file__)[0]) as file:
    # all = file.read().splitlines()
    # last = all[-1]

    max_tokens = 1024

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=f'write a post about {post}',
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].text


if __name__ == '__main__':
    main()
