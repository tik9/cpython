'''Dates Manager
a) Public (German) Holidays like Easter and Pentecost
b) "Individual" dates like anniversary or wedding day
- Time Period from-to and single dates possible
c) Repetitive, "periodical" dates
  '''

from datetime import date, timedelta


# c) repetitive
NAME = 'Abholung'
PERIOD = 2
# 0=monday, 4=friday
SPECIAL_DAY = 4

end_period = date(2025, 2, 7)
freetext_start = 'Wochenende'


def main():
    '''main'''
    # pretty()
    # print(days_to_fr())
    holidays_de()
    # public_holi()


def holidays_de():
    '''weekends'''

    start_period = date(2024, 12, 27)
    holiday_dict = {}
    # holi_add = {}
    # with open('dates.json') as json_file:
        # for key, val in json.load(json_file).items():
            # holiday_dict[parser.parse(key).date()] = val

    event = {}
    event.update(holiday_dict)

    while start_period < end_period:
        start_period = start_period + timedelta(weeks=PERIOD)
        event[start_period] = NAME

    for key, val in sorted(event.items()):
        print(key.strftime('%a %d.%m.%Y'),val)


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


def days_to_fr():
    '''days to special day from a given day'''
    days_to_fr_ = date.today().weekday()-SPECIAL_DAY
    # print(days_to_fr)
    if days_to_fr_ <= 0:
        days_to_fr_ = SPECIAL_DAY-date.today().weekday()
    return days_to_fr_


if __name__ == '__main__':
    main()
