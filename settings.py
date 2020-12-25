from pathlib import Path
import os
import array as arr
import re


def main():
    print('file', __file__)


answers = arr.array('i', [])

picType='.png'
fileSettings = __file__
mdFile = 'python_web_scraping.md'
pic = 'pictures'
home = str(Path.home())
homew = os.path.dirname(os.path.dirname(__file__))
mdFile = os.path.join(os.path.dirname(__file__), mdFile)
pics = os.path.abspath(os.path.join(home, pic))
pl = os.path.join(homew, 'pl')
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
    'Python applied Data Mining', 'Python Web Scraping'
]

if __name__ == "__main__":
    main()
