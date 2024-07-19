#
#  Write a program that asks the user to enter a year and prints whether it's a leap year. A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
