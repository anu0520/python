def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    date = input("Enter Date (mm/dd/yyyy): ")

    try:
        month, day, year = map(int, date.split('/'))

        if year <= 0 or month < 1 or month > 12 or day < 1 or day > 31:
            print("Invalid date format or values.")
            return

        leap_year = is_leap_year(year)

        if leap_year:
            print(f"Given year {year} is a Leap Year")
        else:
            print(f"Given year {year} is a Non Leap Year")

    except ValueError:
        print("Invalid date format. Please enter in mm/dd/yyyy format.")


# Test cases
test_dates = [
    "04/11/19.47",
    "11/15/1936",
    "31/45/1996",
    "64/09/1947",
    "00/00/2000"
]

for date in test_dates:
    print(f"Sample Input: Enter Date : {date}")
    main()
    print()
