from settings import *
from helper import *
from os import path, listdir,remove
import re
import sys
import shutil
import glob
from pathlib import Path
import ntpath

home_w = str(Path.home())
pat='tik9.github.io.git/'
navi='navigation.yml'
nav='_data/'
nav=path.join(home_w,pat,nav,navi)
ext='js'
ext='md'

js_ext='assets' if ext == 'js' else ''
pat=path.join(home_w,pat,js_ext)
    

def main():
    file_=nav
    # str_=renam()
    str_,num=change_co(file_,7)
    print(str_)
    # print(file_)
    # with open(nav, 'w') as f:f.write(str_)


def dele():
    files = glob.glob(f'{pics}/*{pic_type}')
    for f in files:
        remove(f)
        print(f)


def renam():
    mat=''.join([f for f in listdir(pat) if re.match(f'^w\d.{ext}$',f)])
    
    num=int(''.join(filter(str.isdigit, mat)))
    orig=f'w{num}.{ext}'

    orig=path.join(pat,orig)
    # return orig
    
    num+=1
    new=f'w{num}.{ext}'
    new=path.join(pat,new)
    str_=change_co(orig)
    # with open (orig,'r') as f:content=f.read()
    str_=orig+new
    
    # return str_
    # shutil.move(orig,new)
    
def change_co(file_,num=0):
    fil=ntpath.basename(file_)
    if fil !=navi:
        num=int(''.join(filter(str.isdigit, fil)))
    return fil,num

    str_=''
    js='js:'
    with open(file_,'r') as f:
        for line in f:
            
            if '- name: w3 game' in line:
                str_+= f'{line}  link: /w{num}.html\n'
            elif num_b and f'/w{num1}.html' in line:
                continue    
            elif num_b and js in line:
                str_+= f'{js} w{num}\n'
            else:
                str_+=line
    # with open(file_, 'w') as f:f.write(str_)

    return str_

def move():
    # for file in listdir(pics):
        # fullFileName = path.join(pics, file)
        # if re.match(rf'unbenannt\.png\d{{splitter}}\.png$', file.lower()):
            # unbenannt.png28.png
            str='w1.js'
            # str = str.split('.')
            # return(str)
            number = sum(c.isdigit() for c in str)
            # return numbers
            number+=1
            if number ==10: number=1
            str = str[0]
            str_new=f'{str}{number}.js'
            
            localPath = path.dirname(fullFileName)
            file = path.join(localPath, str)
            shutil.move(fullFileName, file)
            print('file', file)


if __name__ == "__main__":
    main()
