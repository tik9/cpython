import settings
import os
import sys
import fnmatch
import string
import re


def check():
    folder = os.path.join(settings.homew, 'lt')

    exclude = ['.git', 'test']
    counter = 1
    contains = ['####', '- [ ]']
    for root, dirs, files in os.walk(folder, topdown=True):
        # for root, dirs, files in os.walk(settings.pics, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        # files=sortfiles(root)
        dirs.sort()
        for name in files:
            if name.endswith('.md') and name.lower() != 'readme.md' and name.lower() != 'contributing.md':
                file = os.path.join(root, name)
                # print(file)
                # if counter == 3:sys.exit()
                counter += 1
                # print(counter)
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    for line in f:
                        str += line

                    if not '####' in str:
                        print(file)


def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def prep2():
    str = ''
    counter = 1
    answers = ['a)', 'b)', 'c)', 'd']
    with open(settings.mdDat, 'r') as f:
        for line in f:
            if line.startswith('Q'):
                str += f'#### {line}'
                continue
            if any(answer in line for answer in answers):
                chara = line.lstrip()[:2]
                str += line.replace(chara, '- []')
                # print(line)

            # str += line
        print(str)
    with open(settings.copy, 'w') as f:    f.write(str)    


def prep():
    str = ''
    counter = 1
    with open(settings.mdDat, 'r') as f:
        for line in f:
            counter += 1
            if '�' in line or '' in line:
                line = line.replace('�', '').replace('', '')
                # print('�')

            if 'Answ' in line:
                continue

            if line.startswith('-') or not line.strip():
                str += line
                continue
            str += line.replace('\n', '')
        print(str)

    with open(settings.mdDat, 'w') as f:
        f.write(str)


settings.init()
# check()
prep2()
