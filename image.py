from PIL import Image
import os
import pytesseract
import sys
import settings


def image():
    # print('ftype','pics','mddat',settings.ftype,settings.pics,settings.mdDat)

    # pytes = r'C:\program files\Tesseract-OCR\tesseract.exe'

    # pytesseract.pytesseract.tesseract_cmd = pytes

    entries = sorted((e for e in os.scandir(settings.pics)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    files = [e.path for e in entries]

    with open(settings.mdDat, "a") as f:
        # for subdir, dirs, files in os.walk(pics):
        # files = [file for file in files if file.endswith(ftype)]
        for file in files:
            if file.lower().endswith(settings.ftype):
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                f.write(text)
                # print(file)
                # print(text)

    # with open(mdDat, 'r') as datei:print(datei.read())


def md():
    with open(settings.mdDat, 'r', encoding="utf8") as f:
        counter = 1
        str = ''
        strChars = ['CO', '', '�', 'oO']
        code = False
        for line in f:

            if 'Answer:' in line or 'Question:' in line:
                continue

            if line in ' \n':
                # print('leer', repr(line))
                continue

            if any(strChar in line for strChar in strChars):
                print(strChar, line)
                # print('komisches Zeichen')
                line = line.replace(strChar, '')

            if line.startswith('?'):
                line = line.replace('?', '')
                str += '\n\n#### '+str(counter)+'. '+line
                counter += 1
                continue

            if '?' in line:
                str += '\n\n#### '+str(counter)+'. '+line
                counter += 1
                continue

            if '```' in line and not code:
                code = True
                continue
            if '```' in line and code:
                code = False
                continue

            if not code:
                str += '- []'+line
            else:
                str += line

            if counter > 5:
                break

        print(str)

    # with open(settings.mdDat, 'w', encoding='utf8') as f:f.write(str)


def qa():
    counta = 0
    countq = 0

    with open(settings.mdDat, "r") as f:
        str = ''
        for line in f:
            if countq == 5:
                break

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

            if counta == answer and countq <= len(settings.answers):
                str += '- [x] '+line[5:]
                continue

            str += line
    print(str)
    # with open(settings.mdDat, 'w') as f:f.write(str)


settings.init()
md()
# qa()
# image()
# code()
