
import datetime
from dateutil import parser
import holidays
from pprint import pp
import re

to_day = datetime.date.today()
end = datetime.date(2023, 7, 13)
# end = datetime.date(2023, 1, 28)
start = datetime.date(2023, 8, 25)
# start = datetime.date(2023, 11, 20)

holi = False
holi = True
typ = 'Max'
typ = 'TK Umgangswochenende'


def main():
    '''main'''
    # pp (to_day.weekday())
    res = date_to_string(holidays_de())
    # res = remove_quotes(res)
    pp(res)


def remove_quotes(dic):
    # d = {'company': 'Wendy\'s Stall'}
    res = "{"+", ".join(["{}:{}".format(k, v) for k, v in dic.items()]) + "}"
    return res


def mytime():
    '''event'''
    days_ahead = 4 - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    friday = to_day + datetime.timedelta(days_ahead)

    counter = 0
    event = {}
    in_between = False
    while friday < end or friday > start and datetime.date(2023, 3, 10) < friday < datetime.date(2023, 12, 1):
        friday = friday+datetime.timedelta(weeks=counter)
        # print(friday>end)
        event[friday] = typ
        counter = 2
        if friday > end and not in_between:
            in_between = True
            days_ahead = 4-start.weekday()
            if days_ahead <= 0:
                days_ahead += 7
            friday = start + datetime.timedelta(days_ahead)

    return event


def holidays_de():
    '''add german - aka "de" - public holidays and kindergarden holidays'''
    holi_add_parse = {}

    for elem in holidays.Germany(years=to_day.year).items():
        if elem[0] < datetime.date(2023, 12, 25) and elem[0] > to_day:
            holi_add_parse[elem[0]] = elem[1]

    holi_add = {
        # '2023-01-27': 'test holi',
        '2023-05-05': 'Betriebsausflug',
        '2023-05-19': 'Brückentag',
        '2023-06-09': 'Pfingstferien',
        '2023-10-02': 'Mein Geburtstag',
        '2023-11-1': 'Alllerheiligen'}

    for k, v in holi_add.items():
        date_ = parser.parse(k).date()
        if date_ < end or date_ > start:
            holi_add_parse[date_] = v
    mytime2 = mytime()
    mytime2.update(holi_add_parse)
    # holi_add_parse.update(event_())
    # pp(dict(holi_add_parse.items()))
    # pp(mytime2)
    return sorted(mytime2.items())


def date_to_string(dict_date):
    '''to string converting'''

    new_dict = {}
    for k, v in dict_date:
        new_elem = k.strftime('%a %d.%m.%Y')
        new_dict[new_elem] = v
    return new_dict


if __name__ == '__main__':
    main()
