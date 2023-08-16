'''Dates Manager
a) Public (German) Holidays like Easter and Pentecost
b) "Individual" dates like anniversary or wedding day
- Time Period from-to and single dates possible
c) Repetitive, "periodical" dates
  '''

from datetime import date, timedelta
import holidays
import json
from prettytable import PrettyTable


# c) repetitive
NAME = 'Abholung'
PERIOD = 2
# 0=monday, 4=friday
SPECIAL_DAY = 4

end_period = date(2024, 1, 15)
freetext_end = 'End'
freetext_start = 'start'


def main():
    '''main'''
    # pretty()
    # print(days_to_fr())
    holidays_de()
    # public_holi()


def holidays_de():
    '''weekends, my friday 16.6.'''
    # holiday_dict = {}
    # holi_add = {}
    # with open('dates.json', encoding='utf-8') as json_file:
    # holi_add = json.load(json_file)

    # for key, val in holi_add.items():
    # holiday_dict[parser.parse(key).date()] = val

    event = {}
    # event.update(holiday_dict)
    date_ = date(2023, 6, 2)

    while date_ < end_period:
        date_ = date_ + timedelta(weeks=PERIOD)
        event[date_] = NAME

    with open('dates.txt', 'w') as f:
        f.write(f'{freetext_start}\n\n')
        for key, val in sorted(event.items()):
            f.write(f"{key.strftime('%a %d.%m.%Y')} {val}\n")
        f.write(freetext_end)


def pretty():
    '''use pretty table'''
    mytab = PrettyTable(['Name', 'Wert (in €)'])
    mytab.align['Name'] = 'l'
    mytab.align['Wert (in €)'] = 'l'
    with open('key_val.txt', 'w') as output:
        output.write(f'Header\n\n')
        sum = 0
        for key, val in values().items():
            sum += float(val)
            mytab.add_row([key.capitalize(), str(val)])
            print(key+' ' + str(val) + '\n')
        output.write(str(mytab))
        print(sum)


def pretty_test():
    '''test pretty table'''
    header = ["City name", "Area"]
    x = PrettyTable(header)
    x.align["City name"] = "l"  # Left align city names
    # One space between column edges and contents (default)
    x.padding_width = 1
    rows = [["Adelaide the city", 1295], ["Brisbane", 5905]]
    with open('key_val.txt', 'w') as out:
        for elem in rows:
            x.add_row(elem)
            print(elem[0], elem[1])
        print(x)
        out.write(str(x))


def values():
    '''get values from json'''
    vals = {}
    file = 'key_val_example.json'
    file = 'income.json'
    file = 'funeral.json'

    with open(file) as json_file:
        vals = json.load(json_file)
    return vals


def public_holi():
    for elem in holidays.Germany(years=date.today().year).items():
        if elem[0] > date(2023, 4, 10):
            print(f'{elem[0]}: {elem[1]}')


def days_to_fr():
    '''days to special day from a given day'''
    days_to_fr_ = date.today().weekday()-SPECIAL_DAY
    # print(days_to_fr)
    if days_to_fr_ <= 0:
        days_to_fr_ = SPECIAL_DAY-date.today().weekday()
    return days_to_fr_


if __name__ == '__main__':
    main()
