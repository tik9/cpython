from pathlib import Path
import os
import shutil
import settings
import re


splitter = 2


def does_string_match(str_):
    # mat = re.match(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    mat = re.match('unbenannt\.png\d{'+str(splitter)+'}\.png$', str_)
    return mat is not None


def cp():

    for file in os.listdir(settings.pics):
        full_file_name = os.path.join(settings.pics, file)
        if does_string_match(file.lower()):
            # unbenannt.png28.png
            str = file.split('.')
            str = str[1][len(str[1])-splitter:]
            str = f'unbenannt{str}{settings.ftype}'
            path = os.path.dirname(full_file_name)
            file = os.path.join(path, str)
            shutil.move(full_file_name, file)
            print('file', file)


settings.init()

cp()
