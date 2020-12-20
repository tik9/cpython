from PIL import Image
import os
import pytesseract
import re
import shutil
import sys

import settings


def does_string_match(str):
    # mat = re.match(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    mat = re.match('unbenannt\.png\d{1,2}\.png$', str)
    return mat is not None


def cp():

    for file in os.listdir(settings.pics):
        fullFileName = os.path.join(settings.pics, file)
        # print(fullFileName)
        if does_string_match(file.lower()):
            # unbenannt.png28.png
            str = file.split('.')
            numbers = sum(c.isdigit() for c in str[1])
            # print(numbers)
            str = str[1][len(str[1])-numbers:]
            str = f'unbenannt{str}{settings.ftype}'
            path = os.path.dirname(fullFileName)
            file = os.path.join(path, str)
            shutil.move(fullFileName, file)
            # print('file', file)


def image():

    files = settings.sortfiles(settings.pics)
    with open(settings.mdDat, 'w') as f:
        for file in files:
            if file.lower().endswith(settings.ftype):
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                f.write(text)
                # print(file)
                print(text)


def mdFormat():
    with open(settings.mdDat, 'r') as f:
        counter = 1
        str = ''

        code = False
        for line in f:

            if line in ' \n' or 'swer:' in line:
                continue

            line = settings.needles(line)

            if line.startswith('?') or '?' in line:

                str, counter = settings.header(str, line, counter)
                continue

            if '```' in line:
                str, code = settings.code(str, code, lang='vb')
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

    with open(settings.mdDat, "r") as f:
        str = ''
        for line in f:

            if line in ' \n':
                continue

            if '##' in line:
                # print(countq)
                str += '\n\n' + line

                if countq >= len(settings.answers):
                    print('no auto solution', countq)
                    countq += 1
                    continue

                answer = settings.answers[countq]
                countq += 1
                counta = 0
                continue

            if '- []' in line:
                counta += 1

            if counta == answer and countq <= len(settings.answers) and '- []' in line:
                str += '- [x] '+line[5:]
                continue

            # if countq == 5:
                # break
            str += line
    # print(str)


settings.init()
# cp()
# image()
str = mdFormat()
# qa()
# print(str)
with open(settings.mdDat, 'w') as f:
    f.write(str)
