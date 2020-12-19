from pathlib import Path
import os
import array as arr
import re


def init():
    global answers, copy, fmode,  ftype, home, homew, mdDat, mdFile, pics

    answers = arr.array('i', [3, 4, 4, 2, 1, 4, 4, 4,
                              4, 1, 4, 1, 2, 2, 4, 2, 3, 1])

    fmode = 'w'
    folder = 'lt'
    ftype = '.png'
    # ftype = '.jpg'
    mdFile = 'angularjs-quiz.md'
    mdFile = 'django-quiz.md'
    copy = 'copy'+mdFile
    pic = 'pictures'
    home = str(Path.home())
    homew = os.path.dirname(os.path.dirname(__file__))
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    copy = os.path.join(os.path.dirname(__file__), copy)
    pics = os.path.abspath(os.path.join(home, pic))
    # pics = home

def needles(line):
    needles = [ '', '�', 'oO', '©']
    nre=re.compile("|".join(map(re.escape, needles)))
    obj=[]
    for needle in nre.finditer(line):
         obj.append(needle)
    return obj

def code(str,code,lang=None):
    if not code:
        str += f'\n```{lang}\n'
        code = True
    else:
        str += '```\n'
        code = False
    return str,code
    
def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]
