from pathlib import Path
import sys

home = str(Path.home())


def main():
    '''main'''
    print(a(4,3))
    # print(home)
    # print(version())


def a(m, n):
    
    v=1
    for i in range(0,n):
        print(v)
        v *= m - i
    
    return v


def version():
    '''version'''
    return [sys.version_info, sys.version_info.major]


if __name__ == "__main__":
    main()
