
import os
from os.path import join
from pathlib import Path
import shutil
import json

home = str(Path.home())
base_folder = os.path.dirname(os.path.dirname(__file__))
# print(base_folder)
folder = join(base_folder, 'fun', 'functions')

js = '.js'
ht = '.html'


def main():
    file_op()
    # copy(join(assets, src+js), join(assets, dst+js))
    pass


def file_op():
    for file in os.listdir(folder):
        os.rename(join(folder, file), join(folder, file[:-3]+'.ts'))
        # print(file[:-3]+'.ts')


def copy(src, dst):
    try:
        shutil.copy(src, dst)
    except IOError:
        print('error')
        with open(join(public, dst), 'w') as f:
            f.write('console.log(1)\n')


def json_():
    with open(public, 'r') as f:
        cont = json.loads(f.read())
        cont.append(dst)
        cont.sort()
        with open(public, 'w') as f:
            json.dump(cont, f, ensure_ascii=False, indent=4)
        # print(cont)


def insert():
    lines = []
    with open('', 'r') as f:
        for line in f:
            lines.append(line)

    lines.append(dst)

    lines.sort()

    # with open(client, 'w') as f:
    # for line in lines:f.write(line + "\n")


if __name__ == "__main__":
    main()
