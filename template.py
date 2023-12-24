from pathlib import Path
import sys
import os
import time

home = str(Path.home())


def main():
    '''main'''
    
    # t=Timer(10, os.system(),'say "ok"')
    # Timer(3, print,"ok").start()
    time.sleep(45*60)
    os.system('say "ok"')

    # Timer(2, os.system('say "ok"')).start()
    # print('\a')

    # print(home)
    # print(version())


def version():
    '''version'''
    return [sys.version_info, sys.version_info.major]


if __name__ == "__main__":
    main()
