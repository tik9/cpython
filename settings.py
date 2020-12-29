from pathlib import Path
import os
import array as arr
import re

homew = os.path.dirname(os.path.dirname(__file__))

gitdir = os.path.join(homew, 'git',)
# os.chdir(gitdir)
# import gitmanager


def main():
    #  'gitmanager'
    print(__file__)
    # from gitdir import commit
    # commit()


answers = arr.array('i', [ 1,2
                          ])
picType = '.png'
fileSettings = __file__
pic = 'pictures'
home = str(Path.home())

example= 'example.md'
mdf = ''
plu = os.path.join(homew, 'pluralsight-skill-tests')
mdFile = os.path.join(plu, mdf)
pics = os.path.abspath(os.path.join(home, pic))

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
    'Python Data Analysis',
    'Python applied Data Mining', 'Python Web Scraping', 'Python Exploratory Data Analysis'
,'Python Exploratory Data Analysis'
]

if __name__ == "__main__":
    main()
