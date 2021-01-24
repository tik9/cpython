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

home = path.dirname(path.dirname(__file__))

custom = path.join(home, '.oh-my-zsh', 'custom')

git_special_dirs = [custom, powershell]


ans_python_data_visual = list('224333113444123433')
answers=list()

pic_type = 'png'
pic_type = 'jpg'
file_settings = __file__
pic = 'pictures'
pic = 'Bilder'
pics = path.join(home, pic)
pics = home

example = path.join(path.dirname(file_settings), 'example.md')
mdf='outlook.md'
mdf='skills.md'
folder=['further-skill-tests','lt','pluralsight-skill-tests']
pa = path.join(home, folder[0])
prod_md = path.join(pa, mdf)

readme = 'README.md'

language='python'
language='nosql'


def main():
    print('prod', prod_md)
    # subprocess.run(['ls', pics])


if __name__ == "__main__":
    main()
