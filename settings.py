from pathlib import Path
from os import path
import subprocess


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


home = str(Path.home())
config = '.config'
powershell = path.join(home, config, 'powershell')
# powershell = path.join(home,'documents','windowspowershell')
user_code = 'Code/User'
user = path.join(home, config, user_code)
# user = path.join(home, 'AppData/Roaming', user_code)

home = '/home/tk'
custom = path.join(home, '.oh-my-zsh', 'custom')


gitSpecialDirs = []
# gitSpecialDirs = [custom, powershell, user]


answers = list('224333113444123433')
# answers = ''.join(n for n in answers)

picType = 'png'
picType = 'jpg'
fileSettings = __file__
pic = 'pictures'
pic = 'Bilder'
pics = path.join(home, pic)
pics = home
picroot = 'unbenannt'
picroot = 'screen01'

example = path.join(path.dirname(fileSettings), 'example.md')
mdf = 'python_data_visualization.md'
plu = path.join(home, 'pluralsight-skill-tests')
prodMd = path.join(plu, mdf)
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
    'Python applied Data Mining', 'Python Web Scraping', 'Python Exploratory Data Analysis', 'Python Clean Data', 'Python Data Visualization'
]


def main():
    print('answer', answers)
    # subprocess.run(['ls', pics])


if __name__ == "__main__":
    main()
