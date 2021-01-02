from pathlib import Path
from os import path
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
gitSpecialDirs = [custom, powershell, user]

answers = [2, 1, 2, 1, 1, 3, 1, 3,
                          1, 4, 3, 2, 1, 2, 1, 2, 4, 3]
picType = '.png'
picType = '.jpg'
fileSettings = __file__
pic = 'pictures'
pic = 'Bilder'

example = path.join(path.dirname(fileSettings),'example.md')
mdf = 'python_clean_data.md'
plu = path.join(home, 'pluralsight-skill-tests')
prodMd = path.join(plu, mdf)
pics = path.join(home, pic)
pics = home
readme = 'README.md'

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
    'Python applied Data Mining', 'Python Web Scraping', 'Python Exploratory Data Analysis', 'Python Clean Data'
]


def main():
    #  'gitmanager'
    print('home', path.dirname(fileSettings))
    # subprocess.run(['ls', pics])


if __name__ == "__main__":
    main()
