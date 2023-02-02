from pathlib import Path
import sys

home = str(Path.home())


def main():
    '''main'''
    print(home)
    print(version())


def content():
    '''content'''
    return 1


def version():
    '''version'''
    return [sys.version_info, sys.version_info.major]


if __name__ == "__main__":
    main()
