#
#  Write a program that asks the user to enter a grade (A, B, C, D, F) and prints a corresponding message (Excellent, Good, Fair, Poor, Fail) using a match-case statement.
grade = input("Enter a grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("Excellent.")
    case "B":
        print("Good.")
    case "C":
        print("Fair.")
    case "D":
        print("Poor.")
    case "F":
        print("Fail.")
    case _:
        print("Invalid grade entered. Please try again.")
