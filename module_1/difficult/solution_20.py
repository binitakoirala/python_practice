#
# Write a program that asks the user to guess a number between 1 and 10, and keeps asking until they guess correctly.
while False:
    number = int(input("Please guess a number: "))
    if number <= 10:
        print(number)
    else:
        print("Incorrect")
    