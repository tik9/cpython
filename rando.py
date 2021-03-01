from settings import *
from helper import *
from itertools import islice
import sys
import re
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from os import listdir, path
from shutil import copy


home_ = str(Path.home())

url = 'https://stackoverflow.com/jobs/508323/softwareentwickler-php-full-stack-entwickler-m-w-hahn-softwareentwicklung'
# url='https://stackoverflow.com/jobs/504942/php-mysql-html-css-js-developers-retail-e-commerce-ventures-llc'
# url='https://stackoverflow.com/jobs/447895/database-reliability-engineer-the-remote-company'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

company_class = 'fc-black-700'
job_class = 'fc-black-900'

company = soup.find('a', class_=company_class).getText()

motivation = 'motivation'
motivation = 'de_' + motivation

pat = path.join(home_, 'downloads', 'PortableJekyll-master', 'bewerbung')
file_job_company = path.join(pat, '_layouts', 'default.html')
main_file = path.join(pat, motivation + '.md')

company_file_name = company.lower().replace(' ', '_')

new_file = path.join(pat, 'moti_' + company_file_name + '.md')

download = path.join(path.dirname(__file__), 'download.txt')

efy_lang = 'expect from you'
efy_lang = 'mitbringen solltest'
line_own = 'expect from me:'
line_own = 'von mir erwarten'


def main():
    str_ = ''
    str_ = job_company(str_)
    # str_ = job_description(str_)
    print(str_)

    with open(file_job_company, 'w', encoding='utf-8') as f:
        f.write(str_)
    # with open(new_file, 'w', encoding='utf-8') as f:f.write(str_)


def job_description(str_):
    wwefy = soup.find_all(text=re.compile(efy_lang))[1].findNext('ul')
    # with open(download, 'a',encoding='utf-8') as f:f.write(wwefy.text)
    # print(main_file,new_file)

    copy(main_file, new_file)

    with open(new_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line_own in line:
                str_ += line + '\n'
                for li in wwefy.find_all('li'):
                    str_ += '- ' + li.text + '\n'
            else:
                str_ += line

    return str_


def job_company(str_):
    sep = '='
    job = soup.find('a', class_=job_class)['title']
    with open(file_job_company, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Id(\'company' in line:
                line = line.split(sep, 1)[0]
                str_ += f'{line} = \'{company}\'\n'
            elif 'Id(\'job' in line:
                line = line.split(sep, 1)[0]
                str_ += f'{line} = \'{job}\'\n'

            else:
                str_ += line

    return str_


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
