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
    print(find())


def find():
    str = '</pre>'
    # str = '[12]'
    link = re.compile(r'\[([^\]]+)\]')
    link = re.compile(r'<[/]?pre>')
    # res = link.findall(str)

    regex = re.match('<[/]?pre>', str)
    # return regex is not None
    return res


def countqa3():
    txt = '''\
    #### Question 1?

    This is the answer 1

    second answer

    #### Another question 2?

    Another answer 2

    #### Question 3?

    Answer 1

    Answer 2

    The Answer 3'''

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


def tail2():
    with open(example) as f:
        print(f.readlines())
    proc = subprocess.Popen(['tail', '-n', 1, example], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines[:, -offset]


def tail(file):
    n = 1
    with open(file) as f:
        pos, lines = 2, []
        while len(lines) <= n:
            try:
                f.seek(-pos, 2)
            except IOError:
                f.seek(0)
                break
            finally:
                lines = list(f)
            pos *= 2
    return ''.join(lines[-n])


def walklevel():
    num_sep = home.count(path.sep)
    for root, dirs, files in walk(home):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


def gitFirstLevel():
    slist = []
    excludedirs = ['.oh-my-zsh', 'doks', 'git']
    # excludedirs = ['.oh-my-zsh', 'doks', 'lt','cv','further-skill-tests','ghpage','my-github-projects','git','ml','pluralsight-skill-tests']

    for root, dirs, files in walklevel():

        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                # print(color.BOLD+root+color.END)
                slist.append(root)
    return slist


def lineAnswer(line, answer, acount):
    if acount == answer:
        line = f'- [x] {line}'
    else:
        line = f'- [] {line}'
    return line


def sortfiles(folder):
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
    # mat = re.match(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    # mat = re.match(f'^{picroot}\.{picType}\d{{1,2}}$', str)
    mat = re.match(search, str)

    return mat is not None


def needles(line):
    needles = ['CO', 'O', '', '�', 'ï¿½', 'ï¿½)' 'oO', '©']
    nre = re.compile("|".join(map(re.escape, needles)))
    obj = []
    for needle in nre.finditer(line):
        line = line.replace(needle.group(0), '')
    return line


if __name__ == "__main__":
    main()
