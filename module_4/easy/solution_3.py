#
# Write a function that takes a list of numbers and returns only the positive ones. Example: filter_positive([-2, 5, -1, 7]) should return [5, 7].
def filter_positive(numbers):
    """
    Returns a new list of positive numbers from the input list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int (list): A list of positive numbers.
    """
    return [num for num in numbers if num >= 0]

numbers = [1, 3, -9, -2, 0]
result= filter_positive(numbers)
print(result)
