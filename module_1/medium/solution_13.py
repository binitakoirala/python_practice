# 
# Write a program that asks the user to enter a day of the week and prints "Weekend" if it's Saturday or Sunday, otherwise prints "Weekday".
day_of_the_week = input("Enter a day of the week: ").lower()

match day_of_the_week:
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Weekday")
