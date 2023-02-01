'''Get every second weekend plus public german holidays and school off'''

from datetime import date, timedelta
from pprint import pp
from dateutil import parser
import holidays


start_summer_vac = date(2023, 8, 7)
end_summer_vac = date(2023, 9, 11)


def main():
    '''main'''
    for key, val in holidays_de():
        print(key.strftime('%a %d.%m.%Y'), val)
    # print((end_summer_vac-start_summer_vac).days)


def days_to_friday(weekday):
    '''days to friday from a given day'''
    days_to_fr = 4 - weekday.weekday()
    if days_to_fr <= 0:
        days_to_fr += 7
    return days_to_fr


def holidays_de():
    '''german public holidays and kindergarden holidays'''
    holi_add_parse = {}

    to_day = date.today()+timedelta(days=7)
    for elem in holidays.Germany(years=to_day.year).items():

        if elem[0] < date(2023, 12, 25) and elem[0] > to_day:
            if elem[1] == 'Karfreitag':
                holi_add_parse[elem[0]] = 'Karfreitag, TK Wochenende'
            else:
                holi_add_parse[elem[0]] = elem[1]

    holi_add = {
        '2023-04-03': 'Kiga geschlossen',
        '2023-05-05': 'Betriebsausflug, TK Wochenende',
        '2023-05-19': 'Brückentag, TK Wochenende',
        '2023-06-09': 'Pfingstferien',
        '2023-06-08': 'Fronleichnam',
        '2023-10-02': 'TK Geburtstag',
        '2023-10-30': 'Beginn Herbstferien',
        '2023-11-03': 'Ende Herbstferien'
    }

    for key, val in holi_add.items():
        holi_add_parse[parser.parse(key).date()] = val

    friday = date(2023, 4, 7)
    event = {}
    while friday < start_summer_vac-timedelta(weeks=2):
        friday = friday+timedelta(weeks=2)
        event[friday] = 'TK Wochenende'

    counter = 7
    while friday < date(2023, 12, 15):
        friday = friday+timedelta(weeks=counter)
        event[friday] = 'TK Wochenende'
        counter = 2
    event.update(holi_add_parse)
    summer = {start_summer_vac: 'Beginn Sommerferien 35 Tage',
              end_summer_vac: 'Ende Sommerferien'}
    event.update(summer)
    return sorted(event.items())


if __name__ == '__main__':
    main()
