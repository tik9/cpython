from os import path, listdir, remove
import re
import shutil
import glob
from pathlib import Path

home = str(Path.home())

prod = False
# prod=True


def main():
    # str_=renam()
    pass

def dele():
    files = glob.glob(f'/*')
    for f in files:
        remove(f)
        print(f)


def move():
    for file in listdir(''):
        fullFileName = path.join('', file)
        if re.match(rf'unbenannt\.png\d{{splitter}}\.png$', file.lower()):
            # unbenannt.png28.png
            str = 'w1.js'
            # str = str.split('.')
            # return(str)
            number = sum(c.isdigit() for c in str)
            # return numbers
            number += 1
            if number == 10:
                number = 1
            str = str[0]
            str_new = f'{str}{number}.js'

            localPath = path.dirname(fullFileName)
            file = path.join(localPath, str)
            shutil.move(fullFileName, file)
            print('file', file)


if __name__ == "__main__":
    main()
