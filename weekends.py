from calendar import weekday
import datetime

date = datetime.datetime.strptime(
    '18.02.2022', '%d.%m.%Y').date()

fridays = []
for i in range(0, 15, 2):
    friday = (date+datetime.timedelta(weeks=i))
    new_friday = friday.strftime('%a %d.%m.%Y')
    fridays.append(new_friday)

today = datetime.date.today()
weekday = today.weekday()
curr_week = datetime.date.today().strftime("%V")
curr_day = datetime.date.today().strftime("%a")
week_after_next_week = (today +
                        datetime.timedelta(weeks=2)).strftime("%V")


print(fridays)
