'''Dates Manager
a) Public (German) Holidays like Easter and Pentecost
b) "Individual" dates like anniversary or wedding day
- Time Period from-to and single dates possible
c) Repetitive, "periodical" dates
  '''

from datetime import date, timedelta
from dateutil import parser
import holidays
import json
from prettytable import PrettyTable


# c) repetitive
NAME = 'Abholung'
PERIOD = 2
# either this friday or next
fr_delta = 7
# 0=monday, 4=friday
SPECIAL_DAY = 4
summer_weeks = 9
weekend_already_set = date(2023, 5, 19)
# TIMEDELTA = 0

# period start on friday
# start_period = date(2023, 4, 7)

interval_period = date(2023, 7, 20)
end_period = date(2023, 12, 15)
freetext = 'End of dates'


def main():
    '''main'''
    pretty()
    # print(days_to_fr())
    # holidays_de()
    # public_holi()


def pretty():
    '''use pretty table'''
    available, vals = values()
    mytab = PrettyTable(['Name', 'Wert (in €)'])
    mytab.align['Name'] = 'l'
    mytab.align['Wert (in €)'] = 'l'
    with open('key_val.txt', 'w') as output:
        output.write(f'verfügbares mtl. EK: {str(available)}\n\n')
        for key, val in vals.items():
            mytab.add_row([key.capitalize(), str(val)])
        print(mytab)

        output.write(str(mytab))


def pretty_test():
    '''test pretty table'''
    x = PrettyTable(["City name", "Area"])
    x.align["City name"] = "l"  # Left align city names
    # One space between column edges and contents (default)
    x.padding_width = 1
    x.add_row(["Adelaide", 1295])
    x.add_row(["Brisbane", 5905])
    print(x)
    with open('key_val.txt', 'w') as out:
        out.write(str(x))


def values():
    '''get values from json'''
    vals = {}
    file = 'key_val.json'
    file = 'key_val_example.json'

    with open(file) as json_file:
        vals = json.load(json_file)
        available = 1
        if file == 'key_val.json':
            available = vals['netto Ek']-vals['Unterhalt'] - vals['nebenkosten'] - \
                vals['versicherungen'] - vals['sonstige Kosten'] - \
                vals['lebenshaltungskosten']
    return available, vals


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


def holidays_de():
    '''german holidays'''
    holiday_dict = {}

    holi_add = {}
    with open('dates.json', encoding='utf-8') as json_file:
        holi_add = json.load(json_file)

    for key, val in holi_add.items():
        holiday_dict[parser.parse(key).date()] = val

    weekday = date.today()+timedelta(days_to_fr())+timedelta(fr_delta)
    event = {}
    while weekday < interval_period-timedelta(weeks=PERIOD):
        weekday = weekday+timedelta(weeks=PERIOD)
        if weekday != weekend_already_set:
            event[weekday] = NAME
    counter = summer_weeks
    while weekday < end_period:
        weekday = weekday+timedelta(weeks=counter)
        event[weekday] = NAME
        counter = PERIOD
    event.update(holiday_dict)

    with open('dates.txt', 'w') as f:
        f.write(f'Header\n\n')
        for key, val in sorted(event.items()):
            f.write(f"{key.strftime('%a %d.%m.%Y')} {val}\n\n")
        f.write(freetext)


if __name__ == '__main__':
    main()
