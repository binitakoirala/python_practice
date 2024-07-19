#
# Write a program that prints the numbers from 1 to 100, but stops if a number is divisible by 17.
i = 1
while i <= 100:
    if i % 17 == 0:
        break
    print(i)
    i+= 1
