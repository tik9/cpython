from settings import *
from helper import *
from itertools import islice
import sys
import os
import re


def main():
    str = ''
    str = rand(str)
    # file, content = check()
    # print(str)
    # print(file)
    with open(prod_md, 'w') as f:f.write(str)


def rand(str):
    # 👍
    # excl = ['<br/>', r'^<[/]?pre>$']
    with open(prod_md, 'r') as f:
        for line in f:
            # m = re.search('Test (.?): Any language', line)
            line = re.sub('^Test (.?): Any language',r'Q\1', line)
            line = re.sub('^Test (\d{1,2}):',r'Q\1', line)
            line=re.sub('(/20\))$',r'\1\n',line)
                # print(m.group(1))

            str += line
    return str


def prep(str):
    # answers = ['a)', 'b)', 'c)', 'd)']
    answers = ['1.', '2.', '3.', '4.']
    codepart = False
    # with open(settings.mdDat, 'r') as f:
    with open(prodMd, 'r') as f:
        for line in f:

            line = line.lstrip()

            # if any(line.startswith(answer) for answer in answers):
            #     # if line.startswith('-'):
            #     chara = line.lstrip()[:3]
            #     if 'Correct'.upper() in line:
            #         line = line.replace(
            #             chara, '- [x] ').replace(' <<<<<--CORRECT ', '')
            #     else:
            #         line = line.replace(chara, '- [] ')
            # if 'Q16.' in line:break
            if line.startswith('Q'):
                line = f'\n\n#### {line}'
            # if '```' in line:line, codepart = code(codepart, lang=language)

            str += line
        return str


def check():

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md',
                   '_config.yml', '.prettierrc']
    contains = ['####', '- [ ]']
    filelist = []
    content = []
    for root, dirs, files in os.walk(lt, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                with open(file, 'r', encoding='UTF8') as f:
                    str_list = list(islice(f, 5))
                    # print(str_list)
                    if not any('####' in s for s in str_list):
                        content.append(str_list)
                        filelist.append(file)

    return filelist, content


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


if __name__ == "__main__":
    main()
