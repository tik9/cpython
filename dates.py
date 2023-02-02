'''Dates Manager
a) Public (German) Holidays like Easter and Pentecost
- double dates possible like easter and gym on same date
b) "Individual" dates like anniversary or wedding day
- Time Period from-to and single dates possible
c) Repetitive, "periodical" dates
  '''

from datetime import date, timedelta
import json
from dateutil import parser
import holidays

# b) individual
JSON = 'dates_example.json'
# JSON = 'dates.json'

dates = [
    {
        date(2023, 8, 7): 'begin intensive training year 2023',
        # date(2023, 8, 7): 'Beginn Sommerferien, Tage: ' + \
        # str((date(2023, 9, 11)-date(2023, 8, 7)).days),
        date(2023, 9, 11): 'end intensive training year 2023',
        # date(2023, 9, 11): 'Ende Sommerferien'
    },
    {
        date(2023, 12, 23): 'Begin online training Python',
        # date(2023, 12, 23): 'Beginn Winterferien, Tage: ' + \
        # str((date(2024, 1, 7)-date(2023, 12, 23)).days),
        date(2024, 1, 7): 'End online training Python'
        # date(2024, 1, 7): 'Ende Winterferien'
    }
]
# dates.append({date(1, 1, 1): '',
#  date(1, 1, 2): ''})


# c) repetitive
# NAME = 'TK Wochenende'
NAME = 'gym'
double_holiday = ['Karfreitag']
PERIOD = 2
SPECIAL_DAY = 4
TIMEDELTA = 7

# period start on friday
start_period = date(2023, 4, 7)
interval_period = date(2023, 8, 7)
end_period = date(2023, 12, 15)


def main():
    '''main'''

    for key, val in holidays_de():
        print(key.strftime('%a %d.%m.%Y'), val)


def days_to_special(weekday):
    '''days to special day from a given day'''
    days_to_fr = SPECIAL_DAY - weekday.weekday()
    if days_to_fr <= 0:
        days_to_fr += 7
    return days_to_fr


def holidays_de():
    '''german public holidays and further holidays'''
    holiday_dict = {}

    for elem in holidays.Germany(years=date.today().year).items():
        holiday_dict[elem[0]] = elem[1]
        if elem[1] in double_holiday:
            holiday_dict[elem[0]] += ' '+NAME

    with open(JSON, encoding='utf-8') as json_file:
        holi_add = json.load(json_file)

    for key, val in holi_add.items():
        holiday_dict[parser.parse(key).date()] = val

    weekday = start_period
    event = {}
    while weekday < interval_period-timedelta(weeks=PERIOD):
        weekday = weekday+timedelta(weeks=PERIOD)
        event[weekday] = NAME

    counter = TIMEDELTA
    while weekday < end_period:
        weekday = weekday+timedelta(weeks=counter)
        event[weekday] = NAME
        counter = PERIOD
    event.update(holiday_dict)

    for elem in dates:
        event.update(elem)

    return sorted(event.items())


if __name__ == '__main__':
    main()
