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

# b) individual
# JSON = 'dates_example.json'
JSON = 'dates.json'

pentecost = date(2023, 6, 9)

holidays_school = [
    {
        date(2023, 7, 31): 'Beginn Sommerferien',
        date(2023, 9, 11): 'Ende Sommerferien'
    },
    {
        date(2023, 12, 23): 'Beginn Winterferien',
        date(2024, 1, 7): 'Ende Winterferien'
    }, {
        date(2023, 10, 30): 'Beginn Herbstferien',
        date(2023, 11, 3): 'Ende Herbstferien'
    }
]

# c) repetitive
NAME = 'Abholung TK'
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
freetext = 'Rückgabe ggf. darauffolgende Sonntag 18 Uhr.'


def main():
    '''main'''
    # print(days_to_fr())
    # holidays_de()
    public_holi()


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
    '''german public holidays and further holidays'''
    holiday_dict = {}

    holi_add = {}
    with open(JSON, encoding='utf-8') as json_file:
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
        f.write(f'Perioden\n\n')
        for key, val in sorted(event.items()):
            f.write(f"{key.strftime('%a %d.%m.%Y')} {val}\n\n")
        f.write(freetext)


if __name__ == '__main__':
    main()
