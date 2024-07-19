#
# Write a function that takes a list of numbers and returns the sum of all even numbers.
numbers = [1,2,3,4,5,6,7,8,9,10]
def sum_even_number (numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

result = sum_even_number(numbers)

print(result)
