from settings import *
import re
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from os import path
from shutil import copy


home_ = str(Path.home())

url = 'https://stackoverflow.com/jobs/397821/software-entwickler-m-w-d-onoffice-gmbh'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

company_class = 'fc-black-700'
job_class = 'fc-black-900'

company = soup.find('a', class_=company_class).getText()
job = soup.find('a', class_=job_class).getText()
company_file_name = company.lower().replace(' ', '_')

efy_lang = 'bringst du mit'
wwefy = soup.find_all(text=re.compile(efy_lang))[1].findNext('ul')

motivation = 'motivation'
motivation = 'de_' + motivation

pat = path.join(home, 'bewerbung')

defaulthtml = path.join(pat, '_layouts', 'default.html')

main_file = path.join(pat, motivation + '.md')

new_file = path.join(pat, 'moti_' + company_file_name + '.md')

download = path.join(path.dirname(__file__), 'download.txt')

efy_lang = 'expect from you'
line_own = 'expect from me:'
line_own = 'von mir erwarten'


def main():
    str_ = ''
    str_ = job_company(str_)
    # str_ = job_description(str_)
    print(job, company, wwefy)

    # with open(new_file, 'w', encoding='utf-8') as f:f.write(str_)


def job_company(str_):
    sep = '='

    with open(defaulthtml, 'r', encoding='utf-8') as f:
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


def job_description(str_):
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


if __name__ == "__main__":
    main()
