
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

# prep()
