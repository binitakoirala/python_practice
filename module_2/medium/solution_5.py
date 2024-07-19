#
# Write a program that asks the user to enter a number of seconds, converts it to hours, minutes, and seconds, and prints the result.
number_in_seconds = int(input("Enter a number in seconds: "))

hours = number_in_seconds // 3600
minutes = (number_in_seconds % 3600) // 60
sec = number_in_seconds % 60

print(f"{hours} hr {minutes} m {sec} s")
