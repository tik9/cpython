import datetime
import holidays
from dateutil import parser
from pprint import pp

to_day = datetime.date.today()
year = to_day.year
holi_dic = holidays.Germany(years=year).items()
str_d_format = '%a %d.%m.%Y'


def main():

    # title = f"Ferientage, Kiga-Schließtage und Umgangswochenenden in {year}\n\n"

    weeknr = 4
    pp(date_to_string(holi_add_dic(weeknr)))
    # pp(event(weeknr))


def event(weeknr):
    weekday = next_weekday(weeknr)
    if weeknr == 4:
        weekday = weekday+datetime.timedelta(days=7)

    counter = 0
    event = {}
    while weekday < datetime.date(2022, 12, 8):

        weekday = weekday+datetime.timedelta(weeks=counter)
        if weekday.month == 8:
            continue
        event[weekday] = 'Umgang'
        # event.append(weekday.strftime(str_d_format))
        counter = 2

    return event


def holi_add_dic(event_inc=0):
    holi_add = {'2022-6-16': 'Fronleichnam',
                '2022-11-1': 'Alllerheiligen', '2022-10-2': 'Geburtstag'}
    holi_add_parse = {}
    for k, v in holi_add.items():
        # print(k, v)
        key = parser.parse(k).date()
        holi_add_parse[key] = v

    for elem in holidays.Germany(years=2022).items():
        if elem[0] > to_day and elem[0] < datetime.date(2022, 12, 10):
            holi_add_parse[elem[0]] = elem[1]

    if event_inc > 0:
        holi_add_parse.update(event(event_inc))
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
    # friday=4
    days_ahead = weekday - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return to_day + datetime.timedelta(days_ahead)


def fridays(count):
    fridays = []
    counter = 0
    for i in range(0, count, 2):
        fri_day = (next_weekday(to_day)+datetime.timedelta(weeks=i))
        new_friday = fri_day.strftime(str_d_format)
        if counter > 0:
            fridays.append(str(counter)+'. '+new_friday)
        counter += 1
    return fridays


def friday_after_break():
    end_kiga = datetime.date(2022, 8, 30)
    next_end_kig = end_kiga+datetime.timedelta(1)
    return next_weekday(next_end_kig)


if __name__ == '__main__':
    main()
