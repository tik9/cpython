from PIL import Image
import os
import pytesseract
import re
import settings
import shutil
import sys


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


def image():

    # print('ftype','pics','mddat',settings.ftype,settings.pics,settings.mdDat)

    # pytes = r'C:\program files\Tesseract-OCR\tesseract.exe'

    # pytesseract.pytesseract.tesseract_cmd = pytes

    entries = sorted((e for e in os.scandir(settings.pics)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    files = [e.path for e in entries]

    with open(settings.mdDat, settings.fmode) as f:
        for file in files:
            if file.lower().endswith(settings.ftype):
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                f.write(text)
                print(file)
                # print(text)


def mdFormat():

    with open(settings.mdDat, 'r', encoding="utf8") as f:
        counter = 1
        str = ''
        needles = ['CO', '', ' ', '�', '� ', 'oO', 'O', 'S', '©']
        needles_re = re.compile("|".join(map(re.escape, needles)))
        code = False
        for line in f:

            if line in ' \n':
                continue

            for m in needles_re.finditer(line):
                # print(m.group(0))
                line = line.replace(m.group(0), '')

            if line.startswith('?'):
                line = line.replace('?', '')
                str += f"\n\n#### {counter}. {line}"
                counter += 1
                continue

            if '?' in line and not code:
                str += f"\n\n#### {counter}. {line}"
                counter += 1
                continue

            if '```' in line and not code:
                str += '\n'
                code = True
                continue
            if '```' in line and code:
                str += '\n'
                code = False
                continue

            if not code:
                str += f"- [] {line}"
            else:
                str += line

            # if counter == 10:
                # break

        # print(str)

    with open(settings.mdDat, 'w', encoding='utf8') as f:
        f.write(str)


def qa():
    counta = 0
    countq = 0

    with open(settings.mdDat, "r") as f:
        str = ''
        for line in f:

            if line in ' \n':
                continue

            if '##' in line:
                # print(countq)
                str += '\n\n' + line

                if countq >= len(settings.answers):
                    print('no auto solution', countq)
                    countq += 1
                    continue

                answer = settings.answers[countq]
                countq += 1
                counta = 0
                continue

            if '- []' in line:
                counta += 1

            if counta == answer and countq <= len(settings.answers) and '- []' in line:
                str += '- [x] '+line[5:]
                continue

            # if countq == 5:
                # break
            str += line
    # print(str)
    with open(settings.mdDat, 'w') as f:        f.write(str)


settings.init()
# cp()
# image()
# mdFormat()
qa()


def prep():
    str = ''
    counter = 1
    with open(settings.mdDat, 'r', encoding='utf8') as f:
        for line in f:
            if '##' in line:
                # line = line.replace('#### ')
                line= re.sub('#### \d+\.', '', line)
                str+=f'#### {counter} {line}' 
                counter += 1
                continue
            str += line
        # print(str)
    with open(settings.mdDat, 'w', encoding='utf8') as f:f.write(str)

# prep()
