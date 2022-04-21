
import os
from os.path import join
from pathlib import Path
import shutil
from pprint import pp
import json

home = str(Path.home())
base_folder = os.path.dirname(os.path.dirname(__file__))

tik = join(base_folder, 'tik')
assets = join(tik, 'assets')
public = join(tik, 'public')
src = 'template'
dst = 'code'
js = '.js'
ht = '.html'
test = join(tik, 'test', 'test.json')


def main():
    # file_op()
    copy(join(assets, src+js), join(assets, dst+js))
    # insert()
    pass


def copy(src, dst):
    try:
        shutil.copy(src, dst)
    except IOError:
        print('error')
        with open(join(assets, dst), 'w') as f:
            f.write('console.log(1)\n')


def json_():
    with open(test, 'r') as f:
        cont = json.loads(f.read())
        cont.append(dst)
        cont.sort()
        with open(test, 'w') as f:
            json.dump(cont, f, ensure_ascii=False, indent=4)
        # print(cont)


def insert():
    lines = []
    with open('', 'r') as f:
        for line in f:
            lines.append(line)

    lines.append(dst)

    lines.sort()
    pp(lines)

    # with open(client, 'w') as f:
    # for line in lines:f.write(line + "\n")


def file_op():
    for file_ in os.listdir(tik):
        print(file_)


if __name__ == "__main__":
    main()
