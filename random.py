from settings import *
from helper import *
from itertools import islice
import sys
import os
import re


def main():
    str = ''
    # str = prep(str)
    # str = prep(str)
    file,str = check()
    print(str)
    # with open(prodMd, 'w') as f:
        # f.write(str)

# re.sub(r'\n+', '\n',x)


def prep(str):
    # answers = ['a)', 'b)', 'c)', 'd)']
    codepart = False
    # with open(settings.mdDat, 'r') as f:
    with open(prodMd, 'r') as f:
        for line in f:

            line = line.lstrip()

            # if line.startswith('Q'):line = f'\n\n#### {line}'
            # if any(line.startswith(answers) for answer in answers):
            if line.startswith('-'):
                chara = line.lstrip()[:2]
                # line = line.replace(chara, '- [] ')
                # print(line)
            if line.startswith('👍'):
                chara = line.lstrip()[:3]
                # line = line.replace(chara, '- [x]')
            if '####' in line:
                line = f'\n\n{line}'
            if '```' in line:
                line, codepart = code(codepart, lang=language)

            str += line
        return str


def rand(str):
    # 👍
    # excl = ['<br/>', r'^<[/]?pre>$']
    with open(prodMd, 'r') as f:
        for line in f:
            # for ex in excl:
            # print(ex, line)
            if re.match(r'^<[/]?pre>$', line) or re.match('.*<br/>', line):
                # print(line)
                continue

            str += line
    return str


def trandom():

    excludeFile = ['.git', 'camera roll', 'saved pictures']
    for root, dirs, files in os.walk(pics):
        dirs[:] = [d for d in dirs if d.lower() not in excludeFile]
        # print(dirs)

        if not any(exclude in root.lower() for exclude in excludeFile):
            # print(root)
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

            if 'Answ' in line or 'Quest' in line:
                continue

            if line.startswith('-') or not line.strip():
                str += line
                continue
            str += line.replace('\n', '')
        return str


def check():

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md']
    contains = ['####', '- [ ]']
    filelist=''
    for root, dirs, files in os.walk(lt, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    str += list(islice(file, 10))

                    if not '####' in str:
                        filelist+=file

    return file,str


if __name__ == "__main__":
    main()
