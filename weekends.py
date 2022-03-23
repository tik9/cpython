from calendar import c
import datetime
import holidays
from pprint import pp
from dateutil import parser

to_day = datetime.date.today()
year = to_day.year


def main():
    # pp(fridays(10))
    # pp(holi())
    title = f"Ferientage, Kiga-Schließtage und Umgangswochenenden in {year} bis August\n"
    with open('file.txt', 'w') as f:
        f.write(title)
        for elem in plus_umgang():
            # pass
            print(elem)
            # f.write(f"{elem}\n")
    # pp(holiday_closingdays())


def holiday_closingdays():
    schliesstage = ['2022-5-13', '2022-5-27', '2022-6-17']
    schliesstag_neu = []
    for elem in schliesstage:
        day = parser.parse(elem).date()
        # day = day.strftime('%a %d.%m.%Y')
        schliesstag_neu.append(day)
        # print(day)
    holi_day = holidays.Germany(years=year).items()
    schliesstag_dic = {el: 'Schließtag' for el in schliesstag_neu}
    schliesstag_dic.update(holi_day)

    return sorted(schliesstag_dic.items())


def plus_umgang():
    event = []
    counter = 2
    for holiday_closing in holiday_closingdays:
            fri_day = (friday()+datetime.timedelta(weeks=counter))
            if fri_day < holiday_closing[0] and fri_day < datetime.date(2022, 8, 5):
                new_friday = fri_day.strftime('%a %d.%m.%Y Umgangswochenende')
                event.append(new_friday)
            if holiday_closing[0] > to_day:
                new_elem = f"{holiday_closing[0].strftime('%a %d.%m.%Y')} {holiday_closing[1]}"
                event.append(new_elem)
                counter += 2
    return event


def holi():
    event = []
    for elem in holidays.Germany(years=2022).items():
        new_elem = f"{elem[0].strftime('%a %d.%m.%Y')} {elem[1]}"
        event.append(new_elem)
    return event


def friday():
    days_ahead = 4 - to_day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return to_day + datetime.timedelta(days_ahead)


def fridays(count):
    fridays = []
    counter = 0
    for i in range(0, count, 2):
        fri_day = (friday()+datetime.timedelta(weeks=i))
        new_friday = fri_day.strftime('%a %d.%m.%Y')
        if counter > 0:
            fridays.append(str(counter)+'. '+new_friday)
        counter += 1
    return fridays


if __name__ == '__main__':
    main()
