from pathlib import Path
from os import path
import subprocess


home_w = str(Path.home())

home_script = path.dirname(path.dirname(__file__))


ans_python_data_visual = list('224333113444123433')
answers = list()

pic_type = 'png'
pic_type = 'jpg'
file_settings = __file__
pic = 'pictures'
pic = 'Bilder'
pics = path.join(home_script, pic)
pics = home_script

example = path.join(path.dirname(file_settings), 'example.md')
mdf = 'outlook/outlook-quiz.md'
folder = ['further-skill-tests', 'lt', 'pluralsight-skill-tests']
pat = path.join(home_script, folder[1])
prod_md = path.join(pat, mdf)

readme = 'README.md'

language = 'python'
language = 'nosql'


def main():
    print('h1,h2', home_w, home_script)

    # subprocess.run(['ls', pics])


if __name__ == "__main__":
    main()
