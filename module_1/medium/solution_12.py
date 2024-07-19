#
# Write a program that asks the user to enter a score and prints "A" for 90 and above, "B" for 80 to 89, "C" for 70 to 79, "D" for 60 to 69, and "F" for below 60.
score = int(input("Please enter a score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
