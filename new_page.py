import sys
from os import path
from pathlib import Path


home=str(Path.home())
path_='tik9.github.io.git'

file_path=path.join(home,path_)

file_='api'
file_up=file_.capitalize()
ext=['js','md']
js=ext[0]
md=ext[1]

file_js=path.join(home,path_,'assets',file_+'1.'+js)
file_md=path.join(home,path_,file_+'1.'+md)
navi_file=path.join(home,path_,'_data/navigation.yml')

prod=False
prod=True


def main():
    str_=''
    str_=navi(str_)
    print(str_)
    if prod:
        with open(navi_file,'w')as f:f.write(str_)

    content()
   

def navi(str_):
    with open(navi_file,'r') as f:
        for line in f:
           if 'Contact' in line:
               str_+=f'- name: {file_up}\n- link: /{file_}.html\n{line}'
           else:
               str_+=line
    return str_

def content():
    str_md=f''' ---\n
layout: default\n
js: {file_}1\n
title: Apis\n
---\n
<div id=api></div> '''

    str_js=""" window.onload=function(){ \n
    console.log(1)\n}
    """
    if prod:
        with open(file_js,'w')as f:f.write(str_js)
    # print(file_md,str_md)


if __name__ == '__main__':
    main()
