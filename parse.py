import os

home_ = str(Path.home())

print(home_w)

file_ = os.path.join(home_w,'tik9.github.io.git', '_data/navigation.yml')


def main():
    str = ''

    str = build(str)

    with open(file_, 'w') as f:f.write(str)
    # print(str)


def build(str):
    with open(file_, 'r') as f:
        for line in f:
            if '' in line:
                str+= f'{line}'
            str += line
    return str


if __name__ == "__main__":
    main()
