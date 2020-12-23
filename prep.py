from settings import *
from helper import *
import os
import re
import sys
import shutil

def main():
    fname,lang,str=fileGen('')
    # cp()
    # check()
    # str = code()
    # str = qa()
    # with open(mdDat, 'a',encoding='UTF8') as f:f.write(str)
    # print(str)
    with open(fname, 'a+') as f:
        f.write(f'## {lang}')
    

def fileGen(str):
    lang = sys.argv[1:] or ['Applied', 'Datamining with Py']
    lang = ' '.join(lang)

    fname = lang.lower().replace(' ', '_')
    
    with open('settings.py', 'r') as f:
        for line in f:
            if 'answers =' in line:
                str+= f'answers = arr.array(\'i\', [ ])'
                continue
            if 'mdFile =' in line:
                # str += f'mdFile =\'{fname}.md\'\n'
                str+=line
                continue
            if re.search(r'\]\n', line):
                # line = line.replace(']', f',\'{lang}\'\n]')
                # str += f',\'{lang}\'\n]'
                str+=line
                continue
            str += line
    return fname,lang, str
    

def cp():
    for file in os.listdir(pics):
        fullFileName = os.path.join(pics, file)
        if does_string_match(file.lower()):
            # unbenannt.png28.png
            str = file.split('.')
            numbers = sum(c.isdigit() for c in str[1])
            # print(numbers)
            str = str[1][len(str[1])-numbers:]
            str = f'unbenannt{str}{ftype}'
            path = os.path.dirname(fullFileName)
            file = os.path.join(path, str)
            shutil.move(fullFileName, file)
            print(file)


def check():
    folder = os.path.join(homew, 'lt')

    excludeDir = ['.git', 'lang']
    excludeFile = ['readme.md', 'contributing.md']
    counter = 1
    contains = ['####', '- [ ]']
    for root, dirs, files in os.walk(folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                counter += 1
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    for line in f:
                        str += line

                    if not '####' in str:
                        print(file)
                        # prep2(file)


def qa(str):
    answers = ['a)', 'b)', 'c)', 'd)', '-']
    code = False
    correct = ' << Correct'
    correct = '👍'
    with open(mdDat, 'r', encoding='UTF8') as f:
        for line in f:

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


def code(str):
    code = False
    with open(mdDat, 'r') as f:
        for line in f:

            if line == '```\n':
                str, code = code(str=str, code=code, lang='python')
                continue

            str += line
    return str


if __name__ == "__main__":
    main()
