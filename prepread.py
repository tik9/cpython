import re
import os
import sys
from settings import *
import glob


readme = os.path.join(plu, readme)

lang = sys.argv[1:] or ['Python', 'Data Visualization']
lang = ' '.join(lang)
file = lang.lower().replace(' ', '_')


def main():
    str = ''

    # str = buildSettings(str)

    # with open(fileSettings, 'w') as f:f.write(str)

    str = buildReadme('')

    with open(readme, 'w') as f: f.write(str)
    # with open(readme, 'r') as f:print(f.read())
    # print(str)


def buildSettings(str):
    files = glob.glob(f'{pics}/*{picType}')
    for f in files:
        # os.remove(f)
        print(f)

    answerNextLine = False
    with open(fileSettings, 'r') as f:
        for line in f:
            if answerNextLine:
                answerNextLine = False
                continue

            if 'answers =' in line:
                line = f'answers = [ ]\n'
                answerNextLine = True
            if 'mdf =' in line:
                line = f'mdf =\'{file}.md\'\n'

            str += line
    return str


def buildReadme(str):

    with open(readme, 'r') as f:
        for line in f:
            if '<!---' in line:
                line = f'- [{lang}]({file}.md)\n{line}'
            str += line
    return str


if __name__ == "__main__":
    main()
