from settings import *
from helper import *
import os
import re
import sys
import shutil
import glob


def main():

    # cp()
    delOldPic()
    # check()
    # str = code()
    # str = qa()
    # with open(mdFile, 'a',encoding='UTF8') as f:f.write(str)
    # print(str)

    # with open(fname, 'w') as f:
    #     f.write(str)


def delOldPic():

    files = glob.glob(f'{pics}/*.png')
    for f in files:
        os.remove(f)
        print(f)


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
            # shutil.move(fullFileName, file)
            print(file)


def code(str):
    code = False
    with open(mdFile, 'r') as f:
        for line in f:

            if line == '```\n':
                str, code = code(str=str, code=code, lang='python')
                continue

            str += line
    return str


if __name__ == "__main__":
    main()
