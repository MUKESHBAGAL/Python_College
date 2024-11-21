def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    """Return the number of days in a given month."""
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # All other months
        return 31


def calculate_start_day(month, year):
    """Calculate the day of the week the month starts on (0=Monday, 6=Sunday)."""
    if month < 3:
        year -= 1
        month += 12
    k = year % 100
    j = year // 100
    return (1 + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7


def generate_calendar(year, border_symbol, months_per_row):
    """Generate the calendar for a year."""
    months = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    column_width = 26  # Width of each month's column
    rows = 12 // months_per_row
    print(f"{year}".center(column_width * months_per_row))
    print()

    for row in range(rows):
        # Print month names
        for col in range(months_per_row):
            month_index = row * months_per_row + col + 1
            if month_index <= 12:
                print(
                    border_symbol + months[month_index].center(column_width - 2) + border_symbol,
                    end="",
                )
            else:
                print(" " * column_width, end="")
        print()

        # Print days of the week
        for col in range(months_per_row):
            print(border_symbol + " ".join(days).center(column_width - 2) + border_symbol, end="")
        print()

        # Print days of each month
        for week in range(6):  # Up to 6 weeks in a month
            for col in range(months_per_row):
                month_index = row * months_per_row + col + 1
                if month_index > 12:
                    continue

                start_day = calculate_start_day(month_index, year)
                days_in_current_month = days_in_month(month_index, year)

                if week == 0:  # First week
                    day_str = "   " * start_day + " ".join(
                        f"{day:2}" for day in range(1, 8 - start_day)
                    )
                else:
                    first_day = week * 7 - start_day + 1
                    last_day = min(first_day + 6, days_in_current_month)
                    day_str = " ".join(
                        f"{day:2}" if first_day <= day <= last_day else "  "
                        for day in range(first_day, first_day + 7)
                    )

                print(border_symbol + day_str.ljust(column_width - 2) + border_symbol, end="")
            print()
        print(border_symbol * (column_width * months_per_row))


# User input and execution
year = int(input("Enter year: "))
#border_symbol = input("Enter border symbol: ")
months_per_row = int(input("Enter number of months per row (e.g., 3, 4): "))

generate_calendar(year, "  ", months_per_row)

