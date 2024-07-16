def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def adjust_anniversary(date_str):
    # Extracting the month, day, and year from the date string
    month, day, year = map(int, date_str.split('/'))

    # Check if the given year is a leap year
    if is_leap_year(year):
        print(f"Given Anniversary Year: Leap Year.")
        next_anniversary_year = year + 1
        print(f"Next Anniversary Date: {month}/{day}/{next_anniversary_year}")
    else:
        print(f"Given Anniversary Year: Non Leap Year.")
        previous_anniversary_year = year - 1
        print(f"Previous Anniversary Date: {month}/{day}/{previous_anniversary_year}")

# Sample input and output
date_str = input("Enter Date (MM/DD/YYYY): ")
adjust_anniversary(date_str)
