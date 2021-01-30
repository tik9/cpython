from settings import *
from os import path, scandir, walk
import re
import sys
import unittest
import subprocess
import fnmatch


def main():
    # print(tail(example))
    listA = countqa2(example)

    # print(listA)
    # print(tail(prodMd), len(listA))
    print(git_first_level())


def countqa3():
    txt = '''\
    #### Question 1?

    This is the answer 1

    second answer

    #### Another question 2?

    Another answer 2'''
    
    pat = re.compile(r'^####.*$\n([\s\S]*?)(?=^####|\Z)', flags=re.M)

    [sum(bool(line.strip()) for line in m.group(1).splitlines())
     for m in pat.finditer(txt)]


def countqa2(mdFile):
    result = []
    with open(mdFile, 'r') as f:

        for line in f:
            line = line.strip()
            if line:  # empty string is False
                if line.startswith('####'):
                    result.append(0)
                elif result:  # empty list is also False
                    result[-1] += 1
    return result


def countqa(mdFile):
    countATotal = []
    tailf = tail(mdFile)

    with open(mdFile, 'r') as f:
        # d=deque(f,maxlen=1)
        qcounter = 0
        acount = 0
        for line in f:

            if line in '\n' or line in ' \n':
                continue

            if '####' in line:

                qcounter += 1
                if qcounter == 2:
                    countATotal.append(acount)
                elif qcounter > 1:
                    countATotal.append(acount)

                acount = 0
                continue
            if '- []' in line or '- [x] ' in line:
                acount += 1
                if line == tailf:
                    countATotal.append(acount)

    return countATotal


def line_answer(line, answer, acount):
    if acount == answer:
        line = f'- [x] {line}'
    else:
        line = f'- [] {line}'
    return line


def sort_files(folder):
    # entries = sorted((e for e in os.scandir(folder)),
    #  key=lambda f: f.name)
    entries = sorted((e for e in scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def code(code, lang=None):
    if not code:
        line = f'\n```{lang}\n'
        code = True
    else:
        line = '```\n'
        code = False
    return line, code


def string_match(search,str):
    # <[/]?pre>
    # mat = re.findall(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    # mat = re.findall(f'^{picroot}\.{picType}\d{{1,2}}$', str)
    mat = re.findall(search, str)

    return mat is not None


def needles(line):
    needles = ['Â© ','O ','© ','Â ','C) ','CO', '', '�', 'ï¿½', 'ï¿½)' 'oO', '©']
    nre = re.compile("|".join(map(re.escape, needles)))
    obj = []
    for needle in nre.finditer(line):
        line = line.replace(needle.group(0), '')
    return line


if __name__ == "__main__":
    main()
