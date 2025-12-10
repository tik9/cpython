'''
Dates Manager
Time Period from-to
Repetitive, "periodical" dates in the period
  '''

from datetime import date, timedelta


def main():
    '''main'''
    next_friday=date.today()+timedelta(days_to_fr())
    next_friday=date(2025,10,31)
    # print(next_friday)
    weekends(next_friday)

def weekends(friday):
    '''weekend'''
    end_period=friday+timedelta(weeks=30)
    event = [[friday,friday+timedelta(days=5)]]
    while friday < end_period:
        friday = friday + timedelta(weeks=2)
        wednes = friday + timedelta(days=5)
        event.append([friday,wednes])

    # print(event)
    for item in event:
        print(item[0].strftime('%a %d.%m.%Y'),item[1].strftime('%a %d.%m.%Y'))

def days_to_fr():
    '''days to special day from a given day'''
    # 0=monday, 4=friday
    SPECIAL_DAY = 4
    return (SPECIAL_DAY-date.today().weekday()+7)%7


if __name__ == '__main__':
    main()
