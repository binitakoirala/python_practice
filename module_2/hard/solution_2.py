#
# Write a program that asks the user to enter a month and prints the season (spring, summer, fall, winter) using a match-case statement.
month = input("Enter a month: ").lower()

match month:
    case "march" | "april" | "may":
        print("Spring Season.")
    case "june" | "july" | "august":
        print("Summer Season.")
    case "september" | "october" | "november":
        print("Fall Season.")
    case "december" | "january" | "february":
        print("Winter Season.")
    case _:
        print("Invalid Month.")
