from settings import *
from helper import *
from itertools import islice
import sys
import os
import re


def main():
    str = ''
    str=prep(str)
    print(str)
    with open(prod_md, 'w') as f:f.write(str)


def rand(str):
    # excl = ['<br/>', r'^<[/]?pre>$']
    with open(prod_md, 'r') as f:
        for line in f:
            # m = re.search('Test (.?): Any language', line)
            line = re.sub('^Test (.?)',r'Q\1', line)
            line = re.sub('^Test (\d{1,2}):',r'Q\1', line)
                # print(m.group(1))

            str += line
    return str


def prep(str):
    with open(prod_md, 'r') as f:
        for line in f:

            if line.startswith('- ['):
                line = line.replace('- []','- [ ]')

            str += line
        return str


def check():

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md']
    filelist = []
    content = []
    for root, dirs, files in os.walk(pat, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                with open(file, 'r') as f:
                    str_list = list(islice(f, 15))
                    # print(str_list)
                    if not any('' in s for s in str_list):
                        content.append(str_list)
                        filelist.append(file)

    return filelist, content


def trandom():

    excludeFile = ['.git', 'camera roll']
    for root, dirs, files in os.walk(pics):
        dirs[:] = [d for d in dirs if d.lower() not in excludeFile]

        if not any(exclude in root.lower() for exclude in excludeFile):
            pass
        for name in files:
            if name.endswith('.png') and not any(exclude in name.lower() for exclude in excludeFile):
                print(name)


def random():
    str = ''
    counter = 1
    with open(mdDat, 'r') as f:
        for line in f:
            counter += 1
            # if '�' in line or '' in line:
            #     line = line.replace('�', '').replace('', '')
            # print('�')
            for m in needles(line):
                line = line.replace(m.group(0), '')

            str += line.replace('\n', '')
        return str


if __name__ == "__main__":
    main()
