from settings import *
from os import path, scandir, walk
import re

def main():
    # print(tail(example))
    list=[1,2,3]
    print(list,'1')
    # print(tail(prodMd), len(listA))


def sort_files(folder):
    # entries = sorted((e for e in os.scandir(folder)),
    #  key=lambda f: f.name)
    entries = sorted((e for e in scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def string_match(search,str):
    mat = re.findall(search, str)

    return mat is not None


if __name__ == "__main__":
    main()
