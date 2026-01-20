'''
Time Period from-to
Repetitive, "periodical" dates in the period
  '''

from datetime import date, timedelta


def main():
    '''main'''
    weekends(date(2026,1,23))

def weekends(friday):
    '''weekend'''
    end_period=friday+timedelta(weeks=10)
    event = [[friday,friday+timedelta(days=5)]]
    while friday < end_period:
        friday = friday + timedelta(weeks=2)
        wednes = friday + timedelta(days=5)
        event.append([friday,wednes])

    for item in event:
        print(item[0].strftime('%a %d.%m.%Y'),item[1].strftime('%a %d.%m.%Y'))

if __name__ == '__main__':
    main()
