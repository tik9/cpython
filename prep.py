import settings
import os
import fnmatch


def check():
    folder = os.path.join(settings.homew, 'lt')

    exclude = ['.git', 'test']
    counter = 1
    contains = ['####', '- [ ]']
    for root, dirs, files in os.walk(folder, topdown=True):
        # for root, dirs, files in os.walk(settings.pics, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        # files=sortfiles(root)
        dirs.sort()
        for name in files:
            if name.endswith('.md') and name.lower() != 'readme.md' and name.lower() != 'contributing.md':
                file = os.path.join(root, name)
                print(file)
                if counter == 3:
                    break
                counter += 1
                with open(file, 'r') as f:
                    for line in f:
                        # if '####' in line:
                        if not any(map(line.__contains__, contains))
                        print(line, file)
                        # break


def sortfiles(folder):
    entries = sorted((e for e in os.scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


def prep():
    str = ''
    counter = 1
    with open(settings.mdDat, 'r', encoding='utf8') as f:
        for line in f:
            if '##' in line:
                # line = line.replace('#### ')
                line = re.sub('#### \d+\.', '', line)
                str += f'#### {counter} {line}'
                counter += 1
                continue
            str += line
        # print(str)
    with open(settings.mdDat, 'w', encoding='utf8') as f:
        f.write(str)


settings.init()
check()
# prep()
