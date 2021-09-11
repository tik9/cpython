import os
from pathlib import Path
from datetime import date, timedelta
from itertools import groupby
from operator import itemgetter

home = str(Path.home())

# print(home)


def main():
    # test()
    allweek()
    # print(list(map(lambda x: x + 1, [1, 2, 3])))


def allweek():
    year = 2021
    d = date(year, 9, 3)
    # First Sunday
    # d += timedelta(days=6 - d.weekday())
    di = {}
    end = date(year + 1, 1, 10)
    end = date(year, 10, 10)
    while d < end:
        di.setdefault(d.strftime('%B'), []).append(str(d))
        # yield d
        # print(d, d.strftime('%B'))

        d += timedelta(days=14)
    for k, v in di.items():
        print(k)
        # list(map(lambda x: x + timedelta(days=2),v))
        for val in v:
            print(val, val+timedelta(days=2))


def test():
    result = []
    sortkeyfn = itemgetter(1)
    input = [('15', 'okt'), ('15', 'sept'), ('1', 'okt')]
    input.sort(key=sortkeyfn)
    for key, valuesiter in groupby(input, key=sortkeyfn):
        result.append(dict(month=key, days=list(v[0] for v in valuesiter)))
    result = {}
    for key, valuesiter in groupby(input, key=sortkeyfn):
        result[key] = list(v[0] for v in valuesiter)
    print(result)


def build(str):
    file_ = os.path.join(home, '')

    with open(file_, 'r') as f:
        for line in f:
            if '' in line:
                str += f'{line}'
            str += line
    return str


if __name__ == "__main__":
    main()
