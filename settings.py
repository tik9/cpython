from pathlib import Path
from os import chdir, getcwd,path
import subprocess


home = str(Path.home())

home_script = path.dirname(path.dirname(__file__))


def main():
    print('h1,h2,cwd', home, home_script,getcwd())
    # chdir(home)
    # subprocess.check_call(['pwd' ])
    # subprocess.check_call(['git', 'status'])


if __name__ == "__main__":
    main()
