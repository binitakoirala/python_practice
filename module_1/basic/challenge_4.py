#
# Write a function that takes a list of numbers and returns a list with each value doubled.
numbers = [1,2,3]
def doubled_value(numbers):
    return [num * 2 for num in numbers]
result = doubled_value(numbers)
print(result)
