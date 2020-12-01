from PIL import Image
import os
import pytesseract
import sys
import settings
import re


def prep():
    counter = 1
    with open(settings.mdDat, 'r', encoding="utf8") as f:
        for line in f:

            if '##' in line:
                line = f"{line[6:]}?"
            print('', line, counter, end='')
            if counter == 10:
                break
            counter += 1


def image():
    # print('ftype','pics','mddat',settings.ftype,settings.pics,settings.mdDat)

    # pytes = r'C:\program files\Tesseract-OCR\tesseract.exe'

    # pytesseract.pytesseract.tesseract_cmd = pytes

    entries = sorted((e for e in os.scandir(settings.pics)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    files = [e.path for e in entries]

    with open(settings.mdDat, "a") as f:
        for file in files:
            if file.lower().endswith(settings.ftype):
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                f.write(text)
                # print(file)
                # print(text)

def md():

    with open(settings.mdDat, 'r', encoding="utf8") as f:
        counter = 1
        str = ''
        needles = ['CO', '', '�', 'oO', 'O', 'S', '©']
        needles_re = re.compile("|".join(map(re.escape, needles)))
        code = False
        for line in f:

            if 'Answer:' in line or 'Question:' in line:
                continue

            if line in ' \n':
                continue

            for m in needles_re.finditer(line):
                # print(m.group(0))
                line = line.replace(m.group(0), '')
                # print('strchar', m.group(0),line)

            if line.startswith('?'):
                line = line.replace('?', '')
                str += f"\n\n#### {counter}. {line}"
                counter += 1
                continue

            if '?' in line:
                str += f"\n\n#### {counter}. {line}"
                counter += 1
                continue

            if 'Which one is not a JavaScript' in line:
                print(line)

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

    with open(settings.mdDat, 'w') as f:
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
    with open(settings.mdDat, 'w') as f:
        f.write(str)


settings.init()
image()
# md()
# qa()
