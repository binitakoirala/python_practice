#
# Write a program that asks the user to enter a temperature in Celsius, converts it to Fahrenheit, and prints the result.
temp_celsius = float(input("Enter a temperatuure in Celsius: "))

fahrenheit = (temp_celsius * 9 / 5) + 32
print(f"{temp_celsius}°C is equal to {fahrenheit}°F")
