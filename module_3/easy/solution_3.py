#
# Write a function display_calendar_month(month, year) that prints the calendar for a given month and year. Use Python's built-in calendar module.
import calendar

year = 2024
month = 8

def display_calendar_month(month, year):
    """
    Prints a calendar for the given month and year.

    Args:
        month (int): The month to display.
        year (int): The year to display.

    Returns:
        None.
    """
    print(calendar.month(year, month))

display_calendar_month(month, year)
