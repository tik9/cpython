from PIL import Image
import os
import pytesseract
import re

from settings import *
from helper import *
import webbrowser

def main():
    str = ''

    # str = image(str,pics)
    str, teststr = mdFormat(str,example)
    print(str, teststr)
    # with open(mdFile, 'w') as f:
        # f.write(str)
    
    # webbrowser.open(mdFile)    
    # os.startfile(mdFile)


def image(str,pics):

    files = sortfiles(pics)
    for file in files:
        if file.lower().endswith(picType):
            img = Image.open(file)
            str += pytesseract.image_to_string(img)
            # print(file)
    return str


def mdFormat(str,mdFile):
    teststr = '\n\n'
    with open(mdFile, 'r') as f:
        qcounter = 0
        tmpqcount = 1
        totacount = 0
        acount = 0
        codepart = False
        answer = 0
        for line in f:

            line = needles(line)
            if line in '\n' or line in ' \n':
                continue

            if line.startswith('?') or '?' in line:
                if line.startswith('?'):
                    line = line.replace('?', '')
                line = f'\n\n#### {qcounter+1}. {line}'

                answer = answers[qcounter]
                qcounter += 1
                acount = 0
                str += line
                continue

            # if qcounter == 2:break
            if '```' in line:
                line, codepart = code(codepart, lang='python')
            if codepart or line.startswith('-'):
                if line.startswith('-'):
                    line = line.replace('-', '')
            else:
                acount += 1
                totacount += 1
                if acount == answer:
                    line = f'- [x] {line}'
                else:
                    line = f'- [] {line}'

                if qcounter > tmpqcount:
                    teststr += f'question: {tmpqcount}, answers: {totacount}. '
                    tmpqcount = qcounter
                    totacount = 0
            str += line
    return str, teststr


if __name__ == '__main__':
    main()
