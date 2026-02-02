
def weekday():
    month = 1
    year = 2026
    q = 1  # 1. Tag

    # Monat/Jahr für Zeller anpassen
    if month < 3:
        m = month + 12
        y = year - 1
    else:
        m = month
        y = year

    K = y % 100
    J = y // 100

    h = (q + (13*(m+1))//5 + K + K//4 + J//4 - 2*J) % 7

    # h: 0=Sam, 1=Son, …, 6=Frei
    # Umwandeln in 0=Sonntag, …, 6=Samstag:
    if h == 0:
        start_day = 6   # Samstag → Index 6
    else:
        start_day = h - 1

    print(start_day)  # 4 → Donnerstag (0=Sonntag)

weekday()

def print_calendar(month, year):
    months = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    monthdays = {
        'January': 31, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31
    }
    month = int(month)
    year = int(year)

    # Leap year check for February
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        monthdays['February'] = 29
    else:
        monthdays['February'] = 28

    # Zeller's Congruence
    # Adjust month and year for formula only
    m = month
    y = year
    if m < 3:
        m += 12
        y -= 1

    k = y % 100  # year of century
    j = y // 100  # zero-based century
    # 1st day of the month
    h = (1 + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7

    # In Zeller: 0 = Saturday, 1 = Sunday, ... 6 = Friday
    # We want 0 = Sunday ... 6 = Saturday
    # Adjust:
    day_of_week = (h + 5) % 7  # This maps 1 (Sunday in Zeller) to 0 (Sunday for us)

    print(f"{months[month]} {year}".center(20))
    print("Su Mo Tu We Th Fr Sa")

    print("   " * day_of_week, end="")
    for day in range(1, monthdays[months[month]] + 1):
        print(f"{day:2} ", end="")
        if (day + day_of_week) % 7 == 0:
            print()

# print_calendar('01', '2026')