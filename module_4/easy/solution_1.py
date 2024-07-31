#
# Write a function that takes a list of numbers and returns the sum of all even numbers. Example: sum_even([1, 2, 3, 4]) should return 6.
def sum_even(numbers):
    """
    Returns the sum of all even numbers in the given list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The sum of all even numbers.
    """
    return sum(num for num in numbers if num % 2 == 0)

result = sum_even([1, 2, 3, 4])
print(result)
