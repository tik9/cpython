import glob
import os
from pathlib import Path
import shutil


home = str(Path.home())
base_folder = os.path.dirname(os.path.dirname(__file__))

tik9 = os.path.join(base_folder, 'tik9')
files = os.path.join(tik9, '')
file_ = ''
clientjs = os.path.join(files, file_)


def main():
    # file_op()
    content = content_file()
    # with open(clientjs, 'w') as f:
    # f.write(content)
    # print(content)


def file_op():
    glob_file = glob.glob(os.path.join(files, file_))
    scriptfile = ''
    new_suffix = '.ts'
    for filename in glob_file:
        scriptfile = filename
        p = Path(scriptfile)
        if p.suffix == '.ts':
            new_suffix = '.js'
        p.rename(Path(p.parent, p.stem + new_suffix))


def copy(scriptfile, new_suffix):
    p = Path(scriptfile)
    dst = os.path.join(p.parent, p.stem+new_suffix)

    shutil.copy(scriptfile, dst)


if __name__ == "__main__":
    main()
