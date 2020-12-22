from settings import *
import os,re,sys

def main():
    init()
    for root, dir, files in os.walk(pics):
        print(files)

def does_string_match(str):
    # mat = re.match(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    mat = re.match('unbenannt\.png\d{1,2}\.png$', str)
    return mat is not None

def header(str, line, counter):
    starter = True if line.startswith('?') else False
    if line.startswith('?'):
        line = line.replace('?', '')
    str += f'\n\n#### {counter}. {line}'
    counter += 1
    return str, counter


def needles(line):
    needles = ['CO', 'O', '', '�', 'ï¿½', 'ï¿½)' 'oO', '©']
    nre = re.compile("|".join(map(re.escape, needles)))
    obj = []
    for needle in nre.finditer(line):
        line = line.replace(needle.group(0), '')
    return line


def code(str, code, lang=None):
    if not code:
        str += f'\n```{lang}\n'
        code = True
    else:
        str += '```\n'
        code = False
    return str, code


def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


if __name__ == "__main__":
    main()