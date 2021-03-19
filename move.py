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
path_='tik9.github.io.git'

pat=path.join(home_w,path_)
ass='assets'
js=path.join(pat,ass)

files=['readme','funct']
trunk=files[0]

trunk_up=trunk.upper() if trunk == readme else trunk
lay_def='_layouts/default.html'

prod=False
# prod=True


def main():
    # str_=renam()
    # file_md=path.join(pat,trunk_up+'.md')
    file_md=path.join(pat,lay_def)
    
    str_=change_co(file_md)
    
    print(str_)
    
    if prod:
        with open(file_md, 'w') as f:f.write(str_)

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
    if prod:shutil.move(orig,new)
    return orig+new
    
def change_co(file_):
    # return num
    str_=''
    p_lay=f'(?<=\<script src={ass}/{trunk})\d(?=\.js>\</script>)'
    # p_lay='(?<=\<script src=assets/readme)\d(?=\.js>\</script>)'
    p_md='(?<=js: [md|gh])\d'
    
    with open(file_,'r') as f:
        for line in f:
            # if 'js: ' in line:
                # str_+= f'js: {trunk}{num}\n'
            if re.findall(p_lay,line):
                str_+=re.sub(p_lay, lambda x: str(int(x.group(0))+1), line)

            else:
                str_+=line
    return str_


def dele():
    files = glob.glob(f'{pics}/*{pic_type}')
    for f in files:
        remove(f)
        print(f)


def move():
    for file in listdir(pics):
        fullFileName = path.join(pics, file)
        if re.match(rf'unbenannt\.png\d{{splitter}}\.png$', file.lower()):
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

def test_reg():
    line = """
    cut into 1-inch florets (about 19cup)
    1cup
    """

    p = '\d+(?=cups?)'
    p='(?<=\<script src=assets/funct)\d(?=\.js>\</script>)'

    line=f'<script src={ass}/funct1.js></script>'

    s=re.sub(p, '\g<1>2\3', line)
    s=re.sub(p, lambda x: str(int(x.group(0))+1), line)
    s=re.findall(p,line)

    print(s)

if __name__ == "__main__":
    main()
