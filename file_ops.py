import glob
import os
from pathlib import Path
import shutil


home = str(Path.home())
base_folder = os.path.dirname(os.path.dirname(__file__))
# dir_path = os.getcwd()

tik9 = os.path.join(base_folder, 'tik9.github.io')
files = tik9
# files = os.path.join(tik9, 'assets')
# file_ = 'client.*'
file_ = 'server.*'


def main():
    scriptfile, new_suffix=getfile()
    rename(scriptfile,new_suffix)
    # copy(scriptfile, new_suffix)

def copy(scriptfile, new_suffix):
    p = Path(scriptfile)
    dst=os.path.join(p.parent,p.stem+new_suffix)

    shutil.copy(scriptfile,dst)

def getfile():
    glob_file = glob.glob(os.path.join(files, file_))
    for filename in glob_file:
        scriptfile = filename
    
    p = Path(scriptfile)
    new_suffix = '.ts'
    if p.suffix == '.ts':
        new_suffix = '.js'
    return scriptfile, new_suffix


def rename(scriptfile, new_suffix):
    p=Path(scriptfile)
    p.rename(Path(p.parent, p.stem + new_suffix))


if __name__ == "__main__":
    main()
