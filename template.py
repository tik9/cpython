import os
from pathlib import Path
import sys

home = str(Path.home())

# print(home)

tik9 = os.path.join(home, 'repo')
folder = os.path.join(tik9, 'fol')
file_ = ''
file_ = os.path.join(folder, file_)


def main():
    content = content_file()
    print(content)


def content_file():
    new_elem = ''
    with open(file_, 'r') as f:
        str_ = ''
        for line in f:
            str_ += line
    return str_


def loop_folder():
    files = []
    for entry in os.scandir(''):
        if entry.name.endswith('.ext'):
            p = Path(entry.name)

            files.append(f"{p.stem}{p.suffix}")
    return files


def version():
    python_ver = sys.version_info
    major = sys.version_info.major
    minor = sys.version_info.minor


if __name__ == "__main__":
    main()
