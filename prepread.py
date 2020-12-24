import os
from settings import *


def main():
    fname = os.path.join(pl, 'README.md')
    str = '## Pluralsight-quiz-questions\n\n<br><br>This repository does not pretend to give you all answers for [Pluralsight Skill questions](https://app.pluralsight.com), rather it is a starting guide to help you prepare for the skills quiz and to know what to expect.<br><br>\n\n'

    str += 'Table of Contents\n\n'

    str = buildlist(str)
    print(str)

    # with open(fname, 'w') as f:
    #     f.write(str)


def buildlist(str):
    for item in langs:
        fname = item.lower().replace(' ', '_')

        str += f'- [{item}]({fname}.md)\n'
    return str


if __name__ == "__main__":
    main()
