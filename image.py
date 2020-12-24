from PIL import Image
import os
import pytesseract
import re

from settings import *
from helper import *


def main():
    str = ''

    # cp()
    # str = image(str)
    # str=mdFormat(str)
    str=qa(str)
    # print(str)
    with open(mdDat, 'w') as f:
        f.write(str)


def image(str):

    files = sortfiles(pics)
    # with open(mdDat, 'w') as f:
    for file in files:
        if file.lower().endswith(ftype):
            img = Image.open(file)
            str += pytesseract.image_to_string(img)
            # print(file)
    return str


def mdFormat(str):
    with open(mdDat, 'r') as f:
        counter = 1

        codepart = False
        for line in f:

            if line in ' \n' or 'swer:' in line:
                continue

            line = needles(line)

            if line.startswith('?') or '?' in line:

                str, counter = header(str, line, counter)
                continue

            if '```' in line:
                str, codepart = code(str, codepart, lang='python')
                continue

            if codepart or line.startswith('-'):
                line = line.replace('-', '')
                str += line

            else:
                str += f"- [] {line}"

            # if counter == 10:
                # break

    return str


def qa(str):
    counta = 0
    countq = 0
    answer=0
    with open(mdDat, "r") as f:
        for line in f:

            if line in ' \n':
                continue

            if '####' in line:
                # print(countq)
                str += '\n\n' + line

                if countq >= len(answers):
                    print('no auto solution', countq)
                    continue

                answer = answers[countq]
                countq += 1
                counta = 0
                continue

            if '- []' in line:
                counta += 1

            if counta == answer and countq <= len(answers) and '- []' in line:
                str += '- [x] '+line[5:]
                continue

            # if countq == 5:
                # break
            str += line
    return str


if __name__ == '__main__':
    main()
