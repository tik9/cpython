import os
from pathlib import Path

home = str(Path.home())

# print(home)

folder = os.path.join(home, 'tik9.github.io')


def main():
    str = ''
    # str = special()
    print(folder)
    loop_folder(folder)


def loop_folder(path):
    for entry in os.scandir(path):
        print(entry.path)


def special(str):
    with open(file_, 'r') as f:
        for line in f:
            if '' in line:
                str += f'{line}'
            str += line
    return str


if __name__ == "__main__":
    main()
