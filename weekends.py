import datetime
import holidays
from dateutil import parser
from pprint import pp

to_day = datetime.date.today()

end = datetime.date(2022, 9, 30)

inc_holidays = True
inc_holidays = False
wednes = True
wednes = False
coming_weekend = True
coming_weekend = False
type_1 = 'max'
all_we = True
all_we = False


def main():
    res = date_to_string(holi_add_dic())
    pp(res)


def event_(type, coming_weekday=False, weekday=4):
    weekday = next_weekday(weekday)
    if not coming_weekday:
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
        for elem in holidays.Germany(years=to_day.year).items():
            if elem[0] > to_day and elem[0] < end:
                holi_add_parse[elem[0]] = elem[1]

        holi_add = {'2022-11-1': 'Alllerheiligen'}

    if type_1 == 'max':
        zusatz = ['2022-10-3']
        zusatz = {key: 'Zusatz' for key in zusatz}
        holi_add.update(zusatz)

    for k, v in holi_add.items():
        date_ = parser.parse(k).date()
        if date_ < end:
            holi_add_parse[date_] = v

    holi_add_parse.update(event_(type_1, coming_weekday=coming_weekend))
    if all_we:
        if type_1 == 'my':
            holi_add_parse.update(event_('max',))
        else:
            holi_add_parse.update(event_('my'))

    if wednes:
        holi_add_parse.update(
            event_('max', coming_weekday=coming_weekend, weekday=2))

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
