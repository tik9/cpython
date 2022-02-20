from http import server
from importlib.resources import path
from mimetypes import suffix_map
import os
from pathlib import Path
import sys

home = str(Path.home())

# print(home)

tik9 = os.path.join(home, 'tik9.github.io')
assets = os.path.join(tik9, 'assets')
file_ = ''


def main():
    # print(loop_folder())
    file_ = os.path.join(tik9, '.js')
    

def loop_folder():
    files = []
    for entry in os.scandir(assets):
        if entry.name.endswith('.js'):
            p = Path(entry.name)

            files.append(f"{p.stem}{p.suffix}")
    return files


def content(str):
    with open(file_, 'r') as f:
        for line in f:
            str += line
    return str


def version():
    python_ver=sys.version_info
    major=sys.version_info.major
    minor=sys.version_info.minor

if __name__ == "__main__":
    main()
