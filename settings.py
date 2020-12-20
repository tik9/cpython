from pathlib import Path
import os
import array as arr
import re


def init():
    global answers, ftype, home, homew, mdDat, pics

    answers = arr.array('i', [3, 4, 4, 2, 1, 4, 4, 4,
                              4, 1, 4, 1, 2, 2, 4, 2, 3, 1])

    ftype = '.png'
    # ftype = '.jpg'
    mdFile = 'angularjs-quiz.md'
    mdFile = 'vba.md'
    pic = 'pictures'
    home = str(Path.home())
    homew = os.path.dirname(os.path.dirname(__file__))
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    pics = os.path.abspath(os.path.join(home, pic, 'vb'))
    # pics = home


def header(str, line, counter):
    starter = True if line.startswith('?') else False
    if line.startswith('?'):
        line = line.replace('?', '')
    str += f'\n\n#### {counter}. {line}'
    counter += 1
    return str, counter


def needles(line):
    needles = ['CO','O', '', '�','ï¿½','ï¿½)' 'oO', '©']
    nre = re.compile("|".join(map(re.escape, needles)))
    obj = []
    for needle in nre.finditer(line):
        line = line.replace(needle.group(0), '')
    return line


def code(str, code, lang=None):
    if not code:
        str += f'\n```{lang}\n'
        code = True
    else:
        str += '```\n'
        code = False
    return str, code


def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]
