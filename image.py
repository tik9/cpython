from PIL import Image
import os
import pytesseract
import re

from settings import *
from helper import *


def main():
    
    init()
    # cp()
    # image()
    str = mdFormat()
    # qa()
    # print(str)
    # with open(mdDat, 'w') as f:
    #     f.write(str)


def image():

    files = sortfiles(pics)
    with open(mdDat, 'w') as f:
        for file in files:
            if file.lower().endswith(ftype):
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                f.write(text)
                # print(file)
                print(text)


def mdFormat():
    with open(mdDat, 'r') as f:
        counter = 1
        str = ''

        code = False
        for line in f:

            if line in ' \n' or 'swer:' in line:
                continue

            line = needles(line)

            if line.startswith('?') or '?' in line:

                str, counter = header(str, line, counter)
                continue

            if '```' in line:
                str, code = code(str, code, lang='vb')
                continue

            if code or line.startswith('-'):
                line = line.replace('-', '')
                str += line

            else:
                str += f"- [] {line}"

            # if counter == 10:
                # break

    return str


def qa():
    counta = 0
    countq = 0

    with open(mdDat, "r") as f:
        str = ''
        for line in f:

            if line in ' \n':
                continue

            if '##' in line:
                # print(countq)
                str += '\n\n' + line

                if countq >= len(answers):
                    print('no auto solution', countq)
                    countq += 1
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
    # print(str)


if __name__ == '__main__':
    main()
        