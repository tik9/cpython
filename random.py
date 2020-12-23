from settings import *
from helper import *


def main():
    random()
    # with open(settings.mdFile, 'w') as f:f.write(str)


def random():
    str = ''
    counter = 1
    with open(mdDat, 'r') as f:
        for line in f:
            counter += 1
            # if '�' in line or '' in line:
            #     line = line.replace('�', '').replace('', '')
            # print('�')
            for m in needles(line):
                line = line.replace(m.group(0), '')

            if 'Answ' in line or 'Quest' in line:
                continue

            if line.startswith('-') or not line.strip():
                str += line
                continue
            str += line.replace('\n', '')
        return str

def check():
    folder = os.path.join(settings.homew, 'lt')

    excludeDir = ['.git', 'test']
    excludeFile = ['readme.md', 'contributing.md']
    counter = 1
    contains = ['####', '- [ ]']
    for root, dirs, files in os.walk(folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in excludeDir]

        dirs.sort()
        for name in files:
            if name.endswith('.md') and not any(exclude in name.lower() for exclude in excludeFile):
                file = os.path.join(root, name)
                # if counter == 3:sys.exit()
                counter += 1
                with open(file, 'r', encoding='UTF8') as f:
                    str = ''
                    for line in f:
                        str += line

                    if not '####' in str:
                        print(file)
                        prep2(file)
    
    return str


def prep2():
    str = ''
    counter = 1
    answers = ['a)', 'b)', 'c)', 'd)']
    code = False
    # with open(settings.mdDat, 'r') as f:
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('Q'):
                str += f'#### {line}'
                continue
            if any(answer in line for answer in answers):
                chara = line.lstrip()[:2]
                str += line.replace(chara, '- []')
                # print(line)
                continue

            if '```' in line and not code:
                str += '\n```\n'
                code = True
                continue
            if '```' in line and code:
                str += '```\n'
                code = False
                continue

            str += line
        return str


if __name__ == "__main__":
    main()
