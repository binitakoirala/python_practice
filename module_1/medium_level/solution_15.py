#
# Write a program that asks the user to enter a month and prints the number of days in that month.
month = input("Enter a month: ").lower()

match month:
    case "february":
        print("February has 28 or 29 days.")
    case "april" | "june" | "september" | "november":
        print(f"{month} has 30 days.")
    case _:
        print(f"{month} has 31 days.")
