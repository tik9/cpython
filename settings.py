from pathlib import Path
import os
import array as arr
import re


answers = arr.array('i', [4,1,2,3,1,1,1,1,4,2,3,1,4,1,4,3,1,3 ])
ftype = '.png'
mdFile = 'applied_data_mining_with_python.md'
# mdFile='settings.py'
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
    print('answ', answers)
