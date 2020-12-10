from pathlib import Path
import os
import array as arr


def init():
    global answers, fmode,  ftype, home, homew,mdDat, mdFile, pics,splitter

    answers = arr.array('i', [])

    fmode = 'w'
    folder='lt'
    ftype = '.png'
    # ftype = '.jpg'
    mdFile = 'visualbasic.md'
    pic = 'pictures/bd'
    splitter = 2
    home = str(Path.home())
    homew=os.path.dirname(os.path.dirname(__file__))
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    pics = os.path.abspath(os.path.join(home, pic))
    
    # pics = home
