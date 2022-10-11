
import datetime
from pprint import pp
import holidays
from dateutil import parser

to_day = datetime.date.today()
end = datetime.date(2022, 12, 14)

holi = True
holi = False
TYP = 'max'
TYP = 'my'


def main():
    '''main'''
    # pp (to_day.weekday())
    res = date_to_string(holi_add_dic())
    pp(res)


def event_(type):
    '''event'''
    days_ahead = 4 - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    weekday= to_day + datetime.timedelta(days_ahead)

    counter = 0
    event = {}
    while weekday < end:
        weekday = weekday+datetime.timedelta(weeks=counter)

        event[weekday] = type
        counter = 2

    return event


def holi_add_dic():
    '''holidays add'''
    holi_add_parse = {}
    holi_add = {}

    if holi:
        for elem in holidays.Germany(years=to_day.year).items():
            if elem[0] > to_day and elem[0] < end:
                holi_add_parse[elem[0]] = elem[1]

        holi_add = {'2022-11-1': 'Alllerheiligen'}

    if TYP == 'max':
        zusatz = ['2022-10-3']
        zusatz = {key: 'Zusatz' for key in zusatz}
        holi_add.update(zusatz)

    for k, v in holi_add.items():
        date_ = parser.parse(k).date()
        if date_ < end:
            holi_add_parse[date_] = v

    holi_add_parse.update(event_(TYP))

    return sorted(holi_add_parse.items())


def date_to_string(dict_date):
    '''to string converting'''
    str_d_format = '%a %d.%m.%Y'

    if isinstance(dict_date, datetime.date):
        return dict_date.strftime(str_d_format)

    new_dict = {}
    for k, v in dict_date:
        new_elem = k.strftime(str_d_format)
        new_dict[new_elem] = v
    return new_dict


if __name__ == '__main__':
    main()
