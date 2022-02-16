import glob
import os
from pathlib import Path

home = str(Path.home())

# print(home)

tik9 = os.path.join(home, 'tik9.github.io')
files = tik9
files = os.path.join(tik9, 'assets')
file_ = 'client.*'


def main():
    glob_file = glob.glob(os.path.join(files, file_))
    for filename in glob_file:
        scriptfile = filename
    p = Path(os.path.join(tik9, scriptfile))
    suffix = '.ts'
    if p.suffix == '.ts':
        suffix = '.js'

    # p.rename(Path(p.parent, p.stem + suffix))


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


if __name__ == "__main__":
    main()
