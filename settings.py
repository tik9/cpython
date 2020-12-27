from pathlib import Path
import os
import array as arr
import re


def main():
    print('file', __file__)


answers = arr.array('i', [1,2,1,2,3,4,4,4,2,2,3,4,2,1,2,1,2,4])

picType='.png'
fileSettings = __file__
mdFile = 'python_web_scraping.md'
pic = 'pictures'
home = str(Path.home())
homew = os.path.dirname(os.path.dirname(__file__))
mdFile = os.path.join(os.path.dirname(__file__), mdFile)
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
    'Python applied Data Mining', 'Python Web Scraping'
]

if __name__ == "__main__":
    main()
