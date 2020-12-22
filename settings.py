from pathlib import Path
import os
import array as arr
import re


# global answers, ftype, home, homew, langs, mdDat, pics

answers = arr.array('i', [3, 4, 4, 2, 1, 4, 4, 4,
                          4, 1, 4, 1, 2, 2, 4, 2, 3, 1])

ftype = '.png'
mdFile = 'applied_data_mining_with_python.md'
pic = 'pictures'
home = str(Path.home())
homew = os.path.dirname(os.path.dirname(__file__))
mdDat = os.path.join(os.path.dirname(__file__), mdFile)
pics = os.path.abspath(os.path.join(home, pic))
# pics = home
langs = [
    'Angular',
    'AngularJs',
    'Aws Big Data',
    'Aws Machine Learning',
    'Building Websites',
    'Building Web Apps with React',
    'Java',
    'Javascript',
    'Mysql',
    'Powershell',
    'Python Core',
    'Python Data Analysis', 'Applied Data Mining with Python'
]


if __name__ == "__main__":
    print('langs', langs)
