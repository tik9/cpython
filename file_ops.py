import glob
import os
from pathlib import Path
import shutil


home = str(Path.home())
base_folder = os.path.dirname(os.path.dirname(__file__))
# dir_path = os.getcwd()

tik9 = os.path.join(base_folder, 'tik9.github.io')
# files = tik9
files = os.path.join(tik9, 'assets')
file_ = 'client.js'
clientjs=os.path.join(files,file_)
# file_ = 'test/radpidapi*'
# file_ = '*.ts'


def main():
    file_op()
    # copy(scriptfile, new_suffix)


def content_file():
    new_elem='tools'
    with open(clientjs, 'r') as f:
        str = ''
        for line in f:
            if '//@ts' in line:
                break
            if ']' in line:
                str+=f'"{new_elem}"'
            str += line
    return sorted(str)

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
