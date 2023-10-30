year = int(input("Year number: "))


def day_of_years(year):
    if year % 100 != 0 and year % 400 == 0:
        return 366
    elif year % 4 == 0:
        return 366
    return 365


print(f"In {year} {day_of_years(year)} days!")
