import datetime
import holidays
from dateutil import parser
from pprint import pp

to_day = datetime.date.today()

end = datetime.date(2022, 5, 30)

inc_holidays = False
wednes = True
wednes = False
coming_wednes = False
coming_wednes = True
type_1 = 'max'
all_we = True
all_we = False


def main():
    res = date_to_string(holi_add_dic())
    pp(res)


def event(type, follow_week=1, weekday=5):
    weekday = next_weekday(weekday)
    if follow_week == 2:
        weekday = weekday+datetime.timedelta(days=7)

    counter = 0
    event = {}
    while weekday < end:

        weekday = weekday+datetime.timedelta(weeks=counter)
        if weekday.month == 8:
            continue

        event[weekday] = type
        counter = 2

    return event


def holi_add_dic():
    holi_add_parse = {}
    holi_add = {}

    if inc_holidays:
        holi_add = {
            '2022-6-16': 'Fronleichnam',
            '2022-11-1': 'Alllerheiligen', '2022-10-2': 'Geburtstag'}

        holi_add_d = ['2022-5-26', '2022-6-16', '2022-10-3']
        holi_add_d = {key: 'Zusatz' for key in holi_add_d}
        holi_add.update(holi_add_d)
        for k, v in holi_add.items():
            date_ = parser.parse(k).date()
            if date_ < end:
                holi_add_parse[date_] = v

        for elem in holidays.Germany(years=to_day.year).items():
            if elem[0] > to_day and elem[0] < end:
                holi_add_parse[elem[0]] = elem[1]

    holi_add_parse.update(event(type_1))
    if all_we:
        if type_1 == 'my':
            holi_add_parse.update(event('max', follow_week=2))
        else:
            holi_add_parse.update(event('my', follow_week=2))

    if wednes:
        if coming_wednes:
            holi_add_parse.update(event('max', weekday=2))
        else:
            holi_add_parse.update(event('max', follow_week=2, weekday=2))

    return sorted(holi_add_parse.items())


def date_to_string(dict_date):
    str_d_format = '%a %d.%m.%Y'

    if isinstance(dict_date, datetime.date):
        return dict_date.strftime(str_d_format)

    new_dict = {}
    for k, v in dict_date:
        new_elem = k.strftime(str_d_format)
        new_dict[new_elem] = v
    return new_dict


def next_weekday(weeknr):
    days_ahead = weeknr - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return to_day + datetime.timedelta(days_ahead)


if __name__ == '__main__':
    main()
