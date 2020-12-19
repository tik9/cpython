
def random():
    str = ''
    counter = 1
    with open(settings.mdDat, 'r') as f:
        for line in f:
            counter += 1
            # if '�' in line or '' in line:
            #     line = line.replace('�', '').replace('', '')
            # print('�')
            for m in settings.needles(line):
                line = line.replace(m.group(0), '')

            if 'Answ' in line or 'Quest' in line:
                continue

            if line.startswith('-') or not line.strip():
                str += line
                continue
            str += line.replace('\n', '')
