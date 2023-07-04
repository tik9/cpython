from pathlib import Path
import os,sys

home = str(Path.home())
doc = "$HOME/documents/"
dw = home+'downloads/'


def main():
    '''main'''
    # print(home)
    content()


def content():
    '''content'''
    file = 'file.py'
    if 'Honorar' in file:
        os.rename(dw+file, doc+'steuer/studienkreis'+file)
    elif 'Gutschrift' in file:
        os.rename(dw+file, doc+'steuer/heytim'+file)
    else:
        print('no file found')

    return 1


def version():
    '''version'''
    return [sys.version_info, sys.version_info.major]


if __name__ == "__main__":
    main()
