
import datetime
from pprint import pp
import holidays
from dateutil import parser

to_day = datetime.date.today()
# end = datetime.date(2023, 12, 14)
end = datetime.date(2023, 7, 20)
start = datetime.date(2023, 8, 20)

holi = False
holi = True
typ = 'max'
typ = 'my'


def main():
    '''main'''
    # pp (to_day.weekday())
    res = date_to_string(holi_add_dic())
    pp(res)

def event_():
    '''event'''
    days_ahead = 4 - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    friday= to_day + datetime.timedelta(days_ahead)

    counter = 0
    event = {}
    # while weekday < end:
    in_between=False
    while friday < end or friday > start and friday<datetime.date(2023,12,16):
        friday = friday+datetime.timedelta(weeks=counter)
        # print(friday>end)
        event[friday] = typ
        counter = 2
        if friday>end and not in_between:
            in_between=True
            days_ahead=4-start.weekday()
            if days_ahead<=0:
                days_ahead+=7
            friday=start+datetime.timedelta(days_ahead)

    return event


def holi_add_dic():
    '''holidays add'''
    holi_add_parse = {}
    holi_add = {}

    if holi:
        for elem in holidays.Germany(years=to_day.year).items():
            if elem[0] > to_day and elem[0] < end or elem[0]>start:
                holi_add_parse[elem[0]] = elem[1]

        holi_add = {'2023-11-1': 'Alllerheiligen'}

    for k, v in holi_add.items():
        date_ = parser.parse(k).date()
        if date_ < end or date_ >start:
            holi_add_parse[date_] = v

    holi_add_parse.update(event_())

    return sorted(holi_add_parse.items())


def date_to_string(dict_date):
    '''to string converting'''

    new_dict = {}
    for k, v in dict_date:
        new_elem = k.strftime('%a %d.%m.%Y')
        new_dict[new_elem] = v
    return new_dict


if __name__ == '__main__':
    main()
