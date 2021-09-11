import os
from pathlib import Path

home = str(Path.home())

print(home)

file_ = os.path.join(home, '')


def main():
    str = ''
    str = special()
    # print(str)


def special(str):
    with open(file_, 'r') as f:
        for line in f:
            if '' in line:
                str += f'{line}'
            str += line
    return str


if __name__ == "__main__":
    main()
