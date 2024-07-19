#
# Write a program that prints the first 10 Fibonacci numbers.
a, b = 0, 1

for i in range(10):
    print(a, end= " ")
    a, b = b, a + b
print()
