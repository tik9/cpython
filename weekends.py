from calendar import c
import datetime
import holidays
from dateutil import parser

to_day = datetime.date.today()
year = to_day.year
holi_dic = holidays.Germany(years=year).items()


def main():
    title = f"Ferientage, Kiga-Schließtage und Umgangswochenenden in {year}\n\n"
    with open('file.txt', 'w') as f:
        # f.write(title)
        for k, v in create_dic():
            date = k.strftime('%a %d.%m')
            print(date, v)
            # f.write(f"{date} {v}\n")


def create_dic():
    schliesstage = ['2022-5-13', '2022-5-27',
                    '2022-6-17', '2022-8-5', '2022-8-30']
    umgang = ['2022-6-3', '2022-9-2', '2022-9-30']
    holi_add = {'2022-6-16': 'Fronleichnam', '2022-11-1': 'Alllerheiligen'}
    schliesstag_parse = []
    for elem in schliesstage:
        schliesstag_parse.append(parser.parse(elem).date())
    schliesstag_dic = {el: 'Schließtag Kiga' for el in schliesstag_parse}

    umgang_parse = []
    for elem in umgang:
        parse_ele=parser.parse(elem).date()
        umgang_parse.append(parse_ele)
        # print(parse_ele)

    umgang_dic = {el: 'Umgang' for el in umgang_parse}
    schliesstag_dic.popitem()
    # schliesstag_dic.update(holi_add)
    schliesstag_dic.update(umgang_dic)
    schliesstag_dic.update(holi_dic)
    return sorted(schliesstag_dic.items())


def single_event():
    fri_day = to_day

    counter = 2
    event = {}
    for holiday_closing in holi_dic:
        if holiday_closing[0] == datetime.date(2022, 5, 1):
            continue
        if holiday_closing[0] < datetime.date(2022, 10, 4) and holiday_closing[0] > to_day:
            event[holiday_closing[0]] = holiday_closing[1]

        fri_day = (next_friday(to_day)+datetime.timedelta(weeks=counter))
        if fri_day > datetime.date(2022, 8, 11) and fri_day < datetime.date(2022, 8, 13):
            counter += 1
        counter += 2

    return sorted(event.items())


def holi():
    event = []
    for elem in holidays.Germany(years=2022).items():
        new_elem = f"{elem[0].strftime('%a %d.%m.%Y')} {elem[1]}"
        event.append(new_elem)
    return event


def next_friday(date):
    days_ahead = 4 - date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return date + datetime.timedelta(days_ahead)


def fridays(count):
    fridays = []
    counter = 0
    for i in range(0, count, 2):
        fri_day = (next_friday(to_day)+datetime.timedelta(weeks=i))
        new_friday = fri_day.strftime('%a %d.%m.%Y')
        if counter > 0:
            fridays.append(str(counter)+'. '+new_friday)
        counter += 1
    return fridays


def friday_after_break():
    end_kiga = datetime.date(2022, 8, 30)
    next_end_kig = end_kiga+datetime.timedelta(1)
    # pp(next_end_kig.strftime('%a %d.%m.%y'))
    return next_friday(next_end_kig)


if __name__ == '__main__':
    main()
