import datetime
import holidays
from dateutil import parser
from pprint import pp

to_day = datetime.date.today()

end = datetime.date(2022, 5, 15)

# example: my_we = true and will be this weekend: we_coming must be true
wednes = False
we_coming = True
we_coming = False
my_we = False
my_we = True


def main():
    pp(date_to_string(holi_add_dic()))


def event(weeknr):
    weekday = next_weekday(weeknr)
    if not we_coming and weeknr == 4:
        weekday = weekday+datetime.timedelta(days=7)

    counter = 0
    event = {}
    while weekday < end:

        weekday = weekday+datetime.timedelta(weeks=counter)
        if weekday.month == 8:
            continue
        if weeknr == 4:
            umgang = 'My WE'
            if not my_we:
                umgang = 'WE Umgang'
        else:
            umgang = 'Mi'
        event[weekday] = umgang
        counter = 2

    return event


def holi_add_dic():
    holi_add = {'2022-6-16': 'Fronleichnam',
                '2022-11-1': 'Alllerheiligen', '2022-10-2': 'Geburtstag'}
    holi_add_d = ['2022-5-26', '2022-6-16', '2022-10-3']
    holi_add_d = {key: 'Zusatz' for key in holi_add_d}

    holi_add.update(holi_add_d)
    holi_add_parse = {}
    for k, v in holi_add.items():
        date_ = parser.parse(k).date()
        if date_ < end:
            holi_add_parse[date_] = v

    for elem in holidays.Germany(years=to_day.year).items():
        if elem[0] > to_day and elem[0] < end:
            holi_add_parse[elem[0]] = elem[1]

    holi_add_parse.update(event(4))

    if wednes == True:
        holi_add_parse.update(event(2))

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


def next_weekday(weekday):
    days_ahead = weekday - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return to_day + datetime.timedelta(days_ahead)


if __name__ == '__main__':
    main()
