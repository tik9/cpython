import datetime
import holidays
from dateutil import parser
from pprint import pp

to_day = datetime.date.today()
year = to_day.year
holi_dic = holidays.Germany(years=year).items()
str_d_format = '%a %d.%m.%Y'


def main():
    pp(date_to_string(holi_add_dic(wednes=True)))


def event(weeknr):
    weekday = next_weekday(weeknr)
    if weeknr != 0:
        weekday = weekday+datetime.timedelta(days=7)

    counter = 0
    event = {}
    while weekday < datetime.date(2022, 12, 8):

        weekday = weekday+datetime.timedelta(weeks=counter)
        if weekday.month == 8:
            continue
        umgang = 'Mi'
        if weeknr == 4:
            umgang = 'WE Umgang'
        event[weekday] = umgang
        counter = 2

    return event


def holi_add_dic(wednes=False):
    holi_add = {'2022-6-16': 'Fronleichnam',
                '2022-11-1': 'Alllerheiligen', '2022-10-2': 'Geburtstag'}
    holi_add2 = ['2022-5-26', '2022-6-16','2022-10-3']
    holi_add3= {key: 'Zusatz' for key in holi_add2}

    holi_add.update(holi_add3)
    holi_add_parse = {}
    for k, v in holi_add.items():
        key = parser.parse(k).date()
        holi_add_parse[key] = v

    for elem in holidays.Germany(years=2022).items():
        if elem[0] > to_day and elem[0] < datetime.date(2022, 12, 10):
            holi_add_parse[elem[0]] = elem[1]

    holi_add_parse.update(event(4))

    if wednes == True:
        holi_add_parse.update(event(2))
    return sorted(holi_add_parse.items())


def date_to_string(dict_date):
    if isinstance(dict_date, datetime.date):
        return dict_date.strftime(str_d_format)

    new_dict = {}
    for k, v in dict_date:
        new_elem = k.strftime(str_d_format)
        new_dict[new_elem] = v
    return new_dict


def next_weekday(weekday):
    days_ahead = weekday - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return to_day + datetime.timedelta(days_ahead)


if __name__ == '__main__':
    main()
