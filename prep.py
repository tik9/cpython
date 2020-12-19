import settings
import os
import sys


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
                # if counter == 10:sys.exit()
                counter += 1
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    for line in f:
                        str += line

                    if not '####' in str:
                        print(file)
                        # prep2(file)


def prep():
    str = ''
    with open(settings.mdDat, 'r') as f:
        for line in f:
            str += line
    return str


def qa():
    str = ''
    answers = ['a)', 'b)', 'c)', 'd)', '-']
    code = False
    correct = ' << Correct'
    correct = '👍'
    with open(settings.mdDat, 'r', encoding='UTF8') as f:
        for line in f:
            if 'Q43' in line:
                break

            if line.startswith('Q'):
                str += f'#### {line}'
                continue
            if any(answer in line for answer in answers):
                chara = line.lstrip()[:2]
                if correct in line:
                    line = line.replace(chara, '- [x] ')
                    str += line
                    continue

                str += line.replace(chara, '- [] ')

                continue

            str += line
        return str


def code():
    str = ''
    code = False
    with open(settings.mdDat, 'r') as f:
        for line in f:

            if line == '```\n':
                str, code = settings.code(str=str, code=code, lang='python')
                print (line)
                continue

            str += line
        return str


settings.init()
# check()
# str = qa()
str = code()
# print(str)
with open(settings.mdDat, 'w',encoding='UTF8') as f:f.write(str)
