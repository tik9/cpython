from settings import *
import os
import re
import sys
import unittest


str1 = 'COTest'
file = 'unbenannt.png.png'
dir = os.path.join(pics, 'bd')
head = ('', '?Hello', 1)
cod = ('', False, 'python')


def main():
    unittest.main()

    # print('sort', sortfiles(dir))
    # entries = (e for e in os.scandir(dir))
    # print([e.path for e in entries])


class TestHelper(unittest.TestCase):

    def test_sortfiles(self):
        self.assertEqual(sortfiles(dir), ['C:\\Users\\User\\pictures\\bd\\unbenannt17.PNG',
                                          'C:\\Users\\User\\pictures\\bd\\unbenannt22.PNG', 'C:\\Users\\User\\pictures\\bd\\unbenannt1.txt'], 'Sort Dir')

    def test_needle(self):
        self.assertEqual(needles(str1), 'Test', "Should remove")

    def test_match(self):
        self.assertEqual(does_string_match(file), False, 'Be false')

    def test_header(self):
        self.assertEqual(header(*head),
                         ('\n\n#### 1. Hello', 2), 'Head Return')

    def test_code(self):
        self.assertEqual(code(*cod), ('\n```python\n', True))


def sortfiles(folder):
    # entries = sorted((e for e in os.scandir(folder)),
    #  key=lambda f: f.name)
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def code(str, code, lang=None):
    if not code:
        str += f'\n```{lang}\n'
        code = True
    else:
        str += '```\n'
        code = False
    return str, code


def header(str, line, counter):
    if line.startswith('?'):
        line = line.replace('?', '')
    str += f'\n\n#### {counter}. {line}'
    counter += 1
    return str, counter


def does_string_match(str):
    # mat = re.match(rf'unbenannt\.png\d{{splitter}}\.png$', str)
    mat = re.match('^unbenannt\.png\d{1,2}\.png$', str)
    return mat is not None


def needles(line):
    needles = ['CO', 'O', '', '�', 'ï¿½', 'ï¿½)' 'oO', '©']
    nre = re.compile("|".join(map(re.escape, needles)))
    obj = []
    for needle in nre.finditer(line):
        line = line.replace(needle.group(0), '')
    return line


if __name__ == "__main__":
    main()
