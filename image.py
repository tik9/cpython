from PIL import Image
import pytesseract
import os
from settings import *
from helper import *


def main():
    str = ''

    # str = image(str,pics)
    str = mdFormat(str,prodMd)
    print(str)

    # with open(prodMd, 'w') as f:f.write(str)
    


def image(str,pics):

    files = sortfiles(pics)
    for file in files:
        if file.lower().endswith(f'.{picType}'):
            img = Image.open(file)
            str += pytesseract.image_to_string(img)
            # print(file)
    return str


def mdFormat(str,mdFile):

    with open(mdFile, 'r') as f:
        qcounter = 0
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
                line = f'\n\n#### {qcounter+1}. {line[3:]}'

                answer = answers[qcounter]
                qcounter += 1
                
                acount = 0
                str += line
                continue

            if '```' in line:
                # line, codepart = code(codepart, lang='python')
                line, codepart = code(codepart, lang=language)
            elif codepart or line.startswith('-'):
                if line.startswith('-'):
                    line = line.replace('-', '')
            else:                
                acount += 1

                line=lineAnswer(line,answer,acount)
                
            str += line
    return str


if __name__ == '__main__':
    main()