from settings import *
from helper import *
from os import path, listdir
import re
import sys
import shutil


def main():

    move()
    # check()
    # str = qa()
    # with open(mdFile, 'a',encoding='UTF8') as f:f.write(str)
    # print(str)

    # with open(fname, 'w') as f:
    #     f.write(str)


def move():
    for file in listdir(pics):
        fullFileName = path.join(pics, file)
        if does_string_match(file.lower()):
            # unbenannt.png28.png
            # screen01.jpg26
            str = file.split('.')
            numbers = sum(c.isdigit() for c in str[1])
            # print(numbers)
            str = str[1][len(str[1]) - numbers:]
            str = f'{picroot[:-2]}{str}.{picType}'
            localPath = path.dirname(fullFileName)
            file = path.join(localPath, str)
            shutil.move(fullFileName, file)
            print('file', file)


if __name__ == "__main__":
    main()
