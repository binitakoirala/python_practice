#
# Write a program that asks the user to enter a day of the week and prints whether it is a weekday or weekend using a match-case statement.
day = input("Please enter a day of the week: ").lower()

match day:
    case "saturday" | "sunday":
        print("It's a Weekend.")
    case _:
        print("It's a Weekday.")
