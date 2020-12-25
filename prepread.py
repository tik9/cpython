import os
import sys
from settings import *

readme = os.path.join(pl, 'README.md')


def main():
    str = ''

    str = buildSettings(str)

    with open(fileSettings, 'w') as f:
        f.write(str)

    str = buildReadme('')

    with open(readme, 'w') as f:
        f.write(str)

    # print(str)


def buildSettings(str):
    lang = sys.argv[1:] or ['Python', 'Web Scraping']
    lang = ' '.join(lang)
    # print('ft', ftype)
    readme = lang.lower().replace(' ', '_')
    answerNextLine = False
    with open(fileSettings, 'r') as f:
        for line in f:
            if answerNextLine:
                answerNextLine = False
                continue

            if 'answers =' in line:
                str += f'answers = arr.array(\'i\', [ ])\n'
                answerNextLine = True
                continue
            if 'mdFile =' in line:
                str += f'mdFile =\'{readme}.md\'\n'
                # str += line
                continue
            if re.search(r'\]\n', line):
                str += f',\'{lang}\'\n]'
                # str += line
                continue
            str += line
    return str


def buildReadme(str):

    str = '## Pluralsight-quiz-questions\n\n<br><br>This repository does not pretend to give you all answers for [Pluralsight Skill questions](https://app.pluralsight.com), rather it is a starting guide to help you prepare for the skills quiz and to know what to expect.<br><br>\n\n'

    str += 'Table of Contents\n\n'

    for item in langs:
        readme = item.lower().replace(' ', '_')

        str += f'- [{item}]({readme}.md)\n'

    str += '\n<br>\n\n### Going further\n\n- [Getting Started](https://github.com/tik9/tesseractToMarkdown) with Tesseract and Python\n\n- [**More** Skill tests not related to Pluralsight](https://github.com/tik9/further-skill-tests)'

    return str


if __name__ == "__main__":
    main()
