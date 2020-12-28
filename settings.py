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
    print(os.listdir())
    # from gitdir import commit
    # commit()


answers = arr.array('i', [1, 1, 1, 3, 1, 3, 1, 1,
                          4, 4, 4, 1, 4, 2, 2, 3, 3, 4])
picType = '.png'
fileSettings = __file__
pic = 'pictures'
home = str(Path.home())
mdFile = 'python_exploratory_data_analysis.md'
pics = os.path.abspath(os.path.join(home, pic))
pl = os.path.join(homew, 'pluralsight-skill-tests')
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
    'Python Data Analysis',
    'Python applied Data Mining', 'Python Web Scraping', 'Python Exploratory Data Analysis'
]
if __name__ == "__main__":
    main()
