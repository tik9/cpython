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

js=path.join(pat,'assets')

files=['w','readme','breakout','gh','se','api','funct']
trunk=files[6]

trunk_up=trunk.upper() if trunk == readme else trunk
prod=False
# prod=True

# line = """
# cut into 1-inch florets (about 19cup)
# 1cup
# """

# p = '\d+(?=cups?)'
p='(?<=\<script src=assets/funct)\d(?=\.js>\</script>)'

# line = 'abcd1abcd'

line='<script src=assets/funct1.js></script>'

# s=re.sub(p, r'\g<1>2\3', line)
s=re.sub(p, lambda x: str(int(x.group(0))+1), line)
# s=re.findall(p,line)

print(s)

sys.exit()

def main():
    num=renam()
    file_md=path.join(pat,trunk_up+'.md')
    file_md=path.join(pat,'_layouts/default.html')
    
    str_=change_co(file_md,num)
    
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
    return num
    
def change_co(file_,num):
    # return num
    str_=''
    p_lay='(?<=\<script src=assets/funct)\d(?=\.js>\</script>)'
    p_md='(?<=js: [md|gh])\d'
    with open(file_,'r') as f:
        for line in f:
            if 'js: ' in line:
                str_+= f'js: {trunk}{num}\n'
            elif re.findall(p_lay,line):
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
