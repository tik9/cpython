import os


home_w = str(Path.home())

print(home_w)

file_ = os.path.join(home_w,'tik9.github.io.git', '_data/navigation.yml')


def main():
    str = ''

    str = build1(str)

    with open(file_, 'w') as f:f.write(str)
    # print(str)


def build1(str):
    newline='- name: foo\n  link: /.html'
    with open(file_, 'r') as f:
        for line in f:
            if 'Contact' in line:
                str+= f'{newline}\n{line}'
            str += line
    return str


def build2(str):
    with open(file_, 'r') as f:
        for line in f:
            pass
    str += line
    return str


if __name__ == "__main__":
    main()
