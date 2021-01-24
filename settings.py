from pathlib import Path
from os import path
import subprocess



home = str(Path.home())
config = '.config'
powershell = path.join(home, config, 'powershell')
# powershell = path.join(home,'documents','windowspowershell')
user_code = 'Code/User'
user = path.join(home, config, user_code)
# user = path.join(home, 'AppData/Roaming', user_code)

home = path.dirname(path.dirname(__file__))

custom = path.join(home, '.oh-my-zsh', 'custom')


ans_python_data_visual = list('224333113444123433')
answers=list()

pic_type = 'png'
pic_type = 'jpg'
file_settings = __file__
pic = 'pictures'
pic = 'Bilder'
pics = path.join(home, pic)
pics = home
picroot = 'unbenannt'
picroot = 'screen01'

example = path.join(path.dirname(file_settings), 'example.md')
mdf ='python_data_in_interpreting.md'
# mdf='nosql/nosql-quiz.md'
plu = path.join(home, 'pluralsight-skill-tests')
# lt = path.join(home, 'lt')
# prodMd = path.join(lt, mdf)
prodMd = path.join(plu, mdf)

readme = 'README.md'

language='python'
language='nosql'


def main():
    print('answer', answers)
    # subprocess.run(['ls', pics])


if __name__ == "__main__":
    main()
