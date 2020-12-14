from pathlib import Path
import os
import array as arr


def init():
    global answers, copy,fmode,  ftype, home, homew,mdDat, mdFile, pics

    answers = arr.array('i', [3,4,4,2,1, 4,4,4,4,1, 4,1,2,2,4, 2,3,1])

    fmode = 'w'
    folder='lt'
    ftype = '.png'
    # ftype = '.jpg'
    mdFile = 'python_data_analysis.md'
    mdFile = 'angularjs-quiz.md'
    copy='copy'+mdFile
    pic = 'pictures'
    home = str(Path.home())
    homew=os.path.dirname(os.path.dirname(__file__))
    mdDat = os.path.join(os.path.dirname(__file__), mdFile)
    copy = os.path.join(os.path.dirname(__file__), copy)
    pics = os.path.abspath(os.path.join(home, pic))
    # pics = home
