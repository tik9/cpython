import re
import os
import sys
from settings import *
import glob


readme = os.path.join(plu, readme)

lang = sys.argv[1:] or ['Python', 'Data Interpreting']
lang = ' '.join(lang)
file = lang.lower().replace(' ', '_')


def main():
    str = ''

    str = buildSettings(str)

    # with open(fileSettings, 'w') as f:f.write(str)

    str = buildReadme('')

    # with open(readme, 'w') as f: f.write(str)
    # with open(readme, 'r') as f:print(f.read())
    print(str)


def buildSettings(str):

    with open(fileSettings, 'r') as f:
        for line in f:

            if 'answers =' in line:
                line = f"answers = list('')\n"
            if 'mdf =' in line:
                line = f'mdf =\'{file}.md\'\n'

            str += line
    return str


def buildReadme(str):
    langs = False
    with open(readme, 'r') as f:
        for line in f:
            if 'Table of Cont' in line:
                langs = True
                line = f'{line}\n\nLanguage|Answers\n-|-'

            if line.startswith('[') and langs:
                line = line[:-2] + '|18 answers\n'

            if '<!---' in line:
                # line = f'- [{lang}]({file}.md)\n{line}'
                langs = False

            str += line
    return str


if __name__ == "__main__":
    main()
