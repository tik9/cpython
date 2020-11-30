from pathlib import Path
import os
import array as arr


def init():
    global answers, ftype, home, mdDat, mdFile, pics
    
    answers = arr.array('i', [4, 1, 4, 2, 4, 4, 2, 3,
                              2, 4, 1, 4, 2, 3, 3, 1, 3, 3])

    ftype = '.png'
    ftype = '.jpg'
    mdFile = 'logic.md'
    # mdFile = 'js.md'
    pic = 'pictures/bd'
    # pic = 'pictures'
    home = str(Path.home())
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    pics = os.path.abspath(os.path.join(home, pic))
    pics = home
    os.chdir(pics)

