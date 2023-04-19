'''Dates Manager
a) Public (German) Holidays like Easter and Pentecost
b) "Individual" dates like anniversary or wedding day
- Time Period from-to and single dates possible
c) Repetitive, "periodical" dates
  '''

from datetime import date, timedelta
import json
from dateutil import parser

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
SPECIAL_DAY = 4
summer_weeks = 9
weekend_exclusion = date(2023, 5, 19)
# TIMEDELTA = 0

# period start on friday
start_period = date(2023, 4, 7)
interval_period = date(2023, 7, 20)
end_period = date(2023, 12, 15)
freetext = 'Die Mittwochstermine bleiben bestehen. Sollte keine "Rückgabe TK" nach einer Abholung genannt sein, ist die Rückgabe der darauffolgende Sonntag 18 Uhr.'


def main():
    '''main'''
    with open('dates.txt', 'w') as f:
        f.write(f'Folgende Perioden wurden für mich gesetzt\n\n')
        for key, val in holidays_de():
            f.write(f"{key.strftime('%a %d.%m.%Y')} {val}\n\n")
        f.write(freetext)


def days_to_special(weekday):
    '''days to special day from a given day'''
    days_to_fr = SPECIAL_DAY - weekday.weekday()
    if days_to_fr <= 0:
        days_to_fr += 7
    return days_to_fr


def holidays_de():
    '''german public holidays and further holidays'''
    holiday_dict = {}

    # for elem in holidays.Germany(years=date.today().year).items():
    # if elem[0] > date(2023, 4, 10):
    # holiday_dict[elem[0]] = elem[1]

    holi_add = {}
    with open(JSON, encoding='utf-8') as json_file:
        holi_add = json.load(json_file)

    for key, val in holi_add.items():
        holiday_dict[parser.parse(key).date()] = val

    weekday = start_period
    event = {}
    while weekday < interval_period-timedelta(weeks=PERIOD):
        weekday = weekday+timedelta(weeks=PERIOD)
        if weekday != weekend_exclusion:
            event[weekday] = NAME
    counter = summer_weeks
    while weekday < end_period:
        weekday = weekday+timedelta(weeks=counter)
        event[weekday] = NAME
        counter = PERIOD
    event.update(holiday_dict)

    return sorted(event.items())


if __name__ == '__main__':
    main()
