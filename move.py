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
pathg='game/'
pat=path.join(home_w,pathg)
navig='navigation.yml'
navi='_data/'
nav=path.join(pat,navi,navig)
js=path.join(pat,'assets')
w='w'
readme='readme'
readme_up=readme.upper()
r_md=path.join(pat,readme_up+'.md')

trunk=readme
# trunk=w

trunk_up= trunk.upper() if trunk == readme else trunk_up=trunk

file_=path.join(pat,trunk_up+'.md')

layou='default.html'
layo='_layouts/'    
lay=path.join(pat,layo,layou)

 
def main():
    num=renam()
    # html,num=renam('html',pat)
    str_=change_co(num)

    print(str_)

    # with open(file_, 'w') as f:f.write(str_)

def renam():
    mat=''.join([f for f in listdir(js) if re.match(f'^{trunk}\d.js$',f)])
    num=int(''.join(filter(str.isdigit, mat)))
    # return num
    orig=f'{trunk}{num}.js'

    orig=path.join(js,orig)
    
    num+=1
    
    if num == 10: num=1
    new=f'{trunk}{num}.js'
    new=path.join(js,new)
    # shutil.move(orig,new)
    return num
    
def change_co(num):
    # return num
    str_=''
    num1=num-1
    with open(file_,'r') as f:
        regex=re.compile('location\.href=\'w.\.html\'')
        for line in f:
            if '- name: w3 game' in line:
                str_+= f'{line}  link: /w{num}.html\n'
            elif f'/w{num1}.html' in line:
                continue    
            elif 'js: ' in line:
                str_+= f'js: {trunk}{num}\n'

            elif re.search(regex,line):
                # print('match')
                str_+=re.sub('\d',str(num),line)
            else:
                str_+=line
        # str_+=str(num)
    return str_


def dele():
    files = glob.glob(f'{pics}/*{pic_type}')
    for f in files:
        remove(f)
        print(f)


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
