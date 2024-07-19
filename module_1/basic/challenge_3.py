#
# Write a function that takes a list of numbers and returns only the positive ones.
numbers = [0,-1,2,-5,8]
def postive_number(numbers):
    return [num for num in numbers if num >= 0]
result = postive_number(numbers)
print(result)
