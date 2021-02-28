from settings import *
from helper import *
from itertools import islice
import sys
import re
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from os import path

home_ = str(Path.home())

url='https://stackoverflow.com/jobs/447895/database-reliability-engineer-the-remote-company'

page=requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

job=soup.find(class_='fc-black-900')['title']
company=soup.find(class_='fc-black-800 employer _up-and-out').getText()
file_=path.join(home_,'tik9.github.io.git','_includes','briefkopf_moti.html')

def main():
    str_ = ''
    str_=rand2(str_)
    
    print(str_)
    # with open(file_),'w') as f: f.write(str_)
    
def rand2(str_):
    sep='='
    with open(file_,'r') as f:
        for line in f:
            if 'company' in line:
                line=line.split(sep,1)[0]
                str_+=f'{line} = \'{company}\'\n'
            elif 'job' in line:
                line=line.split(sep,1)[0]
                str_+=f'{line} = \'{job}\'\n'

            else:
                str_+=line
    
    return str_
    
    
def rand(str):
    # excl = ['<br/>', r'^<[/]?pre>$']
    with open(prod_md, 'r') as f:
        for line in f:
            # m = re.search('Test (.?): Any language', line)
            line = re.sub('^Test (.?)',r'Q\1', line)
                # print(m.group(1))

            str += line
    return str



def check():

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md']
    filelist = []
    content = []
    for root, dirs, files in os.walk(pat, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                with open(file, 'r') as f:
                    str_list = list(islice(f, 15))
                    # print(str_list)
                    if not any('' in s for s in str_list):
                        content.append(str_list)
                        filelist.append(file)

    return filelist, content


def random():

    excludeFile = ['.git', 'camera roll']
    for root, dirs, files in os.walk(pics):
        dirs[:] = [d for d in dirs if d.lower() not in excludeFile]

        if not any(exclude in root.lower() for exclude in excludeFile):
            pass
        for name in files:
            if name.endswith('.png') and not any(exclude in name.lower() for exclude in excludeFile):
                print(name)



if __name__ == "__main__":
    main()
