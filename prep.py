from settings import *
from helper import *
import os
import re
import sys
import shutil


def main():
    fname, lang, str = fileGen('')
    # cp()
    # check()
    # str = code()
    # str = qa()
    # with open(mdDat, 'a',encoding='UTF8') as f:f.write(str)
    print(fname)
    # with open(fname, 'a+') as f:
    #     f.write(f'## {lang}')


def fileGen(str):
    lang = sys.argv[1:] or ['Applied', 'Datamining with Py']
    lang = ' '.join(lang)

    fname = lang.lower().replace(' ', '_')

    with open('settings.py', 'r') as f:
        for line in f:
            if 'answers =' in line:
                str += f'answers = arr.array(\'i\', [ ])'
                continue
            if 'mdFile =' in line:
                # str += f'mdFile =\'{fname}.md\'\n'
                str += line
                # fname = line.replace('mdFile = \'', '').replace(
                    "'", '').replace('\n', '')
                continue
            if re.search(r'\]\n', line):
                # str += f',\'{lang}\'\n]'
                str += line
                continue
            str += line
    return fname, lang, str


def cp():
    for file in os.listdir(pics):
        fullFileName = os.path.join(pics, file)
        if does_string_match(file.lower()):
            # unbenannt.png28.png
            str = file.split('.')
            numbers = sum(c.isdigit() for c in str[1])
            # print(numbers)
            str = str[1][len(str[1])-numbers:]
            str = f'unbenannt{str}{ftype}'
            path = os.path.dirname(fullFileName)
            file = os.path.join(path, str)
            shutil.move(fullFileName, file)
            print(file)



def code(str):
    code = False
    with open(mdDat, 'r') as f:
        for line in f:

            if line == '```\n':
                str, code = code(str=str, code=code, lang='python')
                continue

            str += line
    return str


if __name__ == "__main__":
    main()
