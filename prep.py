import settings
import os
import sys
import fnmatch
import string
import re


def check():
    folder = os.path.join(settings.homew, 'lt')

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md']
    counter = 1
    contains = ['####', '- [ ]']
    for root, dirs, files in os.walk(folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                # if counter == 3:sys.exit()
                counter += 1
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    for line in f:
                        str += line

                    if not '####' in str:
                        print(file)
                        prep2(file)


def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def prep2():
    str = ''
    counter = 1
    answers = ['a)', 'b)', 'c)', 'd)']
    code = False
    # with open(settings.mdDat, 'r') as f:
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('Q'):
                str += f'#### {line}'
                continue
            if any(answer in line for answer in answers):
                chara = line.lstrip()[:2]
                str += line.replace(chara, '- []')
                # print(line)
                continue

            if '```' in line and not code:
                str += '\n```\n'
                code = True
                continue
            if '```' in line and code:
                str += '```\n'
                code = False
                continue

            str += line
        print(str)
    # with open(settings.mdFile, 'w') as f:f.write(str)


def prep():
    str = ''
    counter = 1
    with open(settings.mdDat, 'r') as f:
        for line in f:
            counter += 1
            # if '�' in line or '' in line:
            #     line = line.replace('�', '').replace('', '')
            # print('�')
            for m in settings.needles().finditer(line):
                line = line.replace(m.group(0), '')

            if 'Answ' in line or 'Quest' in line:
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
prep()
