from pathlib import Path
from os import path
import array as arr
import re
import subprocess

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

home = str(Path.home())

custom = path.join(home, '.oh-my-zsh', 'custom')

config = '.config'
powershell = path.join(home, config, 'powershell')
user_code = 'Code/User'
user = path.join('C:/Users/User/AppData/Roaming', user_code)
user = path.join(home, config, user_code)
# gitSpecialDirs = [custom, powershell,user]
gitSpecialDirs = [user]


answers = arr.array('i', [1, 2
                          ])
picType = '.png'
fileSettings = __file__
pic = 'pictures'
pic = 'Bilder'

example = 'example.md'
mdf = ''
plu = path.join(home, 'pluralsight-skill-tests')
mdFile = path.join(plu, mdf)
pics = path.join(home, pic)
readme='README.md'

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
    'Python applied Data Mining', 'Python Web Scraping', 'Python Exploratory Data Analysis', 'Python Exploratory Data Analysis'
]


def main():
    #  'gitmanager'
    print('home', home, gitSpecialDirs)
    # subprocess.run('ls',pics)
    # from gitdir import commit
    # commit()


if __name__ == "__main__":
    main()
