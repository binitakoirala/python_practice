#
# Write a program that prints all prime numbers between 1 and 100.
prime_numbers = []
for num in range(1, 101):
    if num == 1:
        continue
    elif num ==2:
        prime_numbers.append(num)
    count = 0
    for i in range(2, num //2 + 2):
        if num % i == 0:
            count += 1

    if count == 0:
        prime_numbers.append(num)
print(prime_numbers)
