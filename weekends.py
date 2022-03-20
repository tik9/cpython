from calendar import c
import datetime


def main():
    # d = datetime.date(2022, 3, 20)
    next = friday()
    all_fridays = fridays(next)
    print(next, all_fridays)


def fridays(next):
    fridays = []
    counter = 0
    for i in range(0, 11, 2):
        friday = (next+datetime.timedelta(weeks=i))
        new_friday = friday.strftime('%a %d.%m.%Y')
        if counter > 0:
            fridays.append(str(counter)+'. '+new_friday)
        counter += 1
    return fridays


def friday():
    d = datetime.date.today()
    days_ahead = 4 - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


if __name__ == '__main__':
    main()
