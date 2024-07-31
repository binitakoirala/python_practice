#
# Write a function that finds the maximum value in a list of numbers without using the `max` function. Example: find_maximum([1, 3, 2]) should return 3.
def maximum_value(numbers):
    """
    Returns the maximum value from a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns (int): The maximum value in the list.
    """
    max_value = numbers[0]
    for value in numbers:
        if value > max_value:
            max_value = value
    return max_value

result = maximum_value([10, 19, 6, 11])
print(result)
