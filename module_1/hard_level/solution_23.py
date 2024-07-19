#
# Write a program that asks the user to enter three numbers and prints the largest number.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 >= number2:
    if number1 >= number3:
        print("The largest number is:", number1)
    else:
        print("The largest number is:", number3)

else:
    if number2 >= number3:
        print("The largest number is:", number2)
    else:
        print("The largest number is:", number3)

# print("The largest number is:", largest_number)
