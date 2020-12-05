from pathlib import Path
import os
import array as arr


def init():
    global answers, fmode, ftype, home, mdDat, mdFile, pics

    answers = arr.array('i', [4, 3, 2, 1, 3, 2, 4, 2,
                              1, 3, 1, 4, 1, 4, 3, 1, 4, 1])

    fmode = "a"
    ftype = '.png'
    ftype = '.jpg'
    mdFile = 'py_vb_proj_linux.md'
    mdFile = 'angularjs.md'
    pic = 'pictures/bdpm'
    home = str(Path.home())
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    pics = os.path.abspath(os.path.join(home, pic))
    pics = home
