import os
import sys
from settings import *

readme = os.path.join(plu, readme)


def main():
    str = ''

    str = buildSettings(str)

    # with open(fileSettings, 'w') as f:f.write(str)

    str = buildReadme('')

    with open(readme, 'w') as f: f.write(str)

    # print(str)


def buildSettings(str):
    lang = sys.argv[1:] or ['Python', 'Clean Data']
    lang = ' '.join(lang)
    # print('ft', ftype)
    file = lang.lower().replace(' ', '_')
    answerNextLine = False
    with open(fileSettings, 'r') as f:
        for line in f:
            if answerNextLine:
                answerNextLine = False
                continue

            if 'answers =' in line:
                line = f'answers = arr.array(\'i\', [ ])\n'
                answerNextLine = True
            if 'mdf =' in line:
                line = f'mdf =\'{file}.md\'\n'
            if re.match(r']\n', line):
            # if line in '\n]\n':
                line = f',\'{lang}\'\n]\n'
            str += line
    return str


def buildReadme(str):

    str = '## Pluralsight-quiz-questions\n\n<br><br>This repository does not pretend to give you all answers for [Pluralsight Skill questions](https://app.pluralsight.com), rather it is a starting guide to help you prepare for the skills quiz and to know what to expect.<br><br>\n\n'

    str += '### Table of Contents\n\n'

    for item in langs:
        mdFile = item.lower().replace(' ', '_')

        str += f'- [{item}]({mdFile}.md)\n'

    str += '\n<br>\n\n### Going further\n\n- [Getting Started](https://github.com/tik9/tesseractToMarkdown) with Tesseract and Python\n\n- [More Skill tests not related to Pluralsight](https://github.com/tik9/further-skill-tests)'

    return str


if __name__ == "__main__":
    main()
