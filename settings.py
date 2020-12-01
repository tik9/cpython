from pathlib import Path
import os
import array as arr


def init():
    global answers, ftype, home, mdDat, mdFile, pics
    
    answers = arr.array('i', [])

    ftype = '.png'
    mdFile = 'logic.md'
    pic = 'pictures/bd1'
    home = str(Path.home())
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    pics = os.path.abspath(os.path.join(home, pic))

