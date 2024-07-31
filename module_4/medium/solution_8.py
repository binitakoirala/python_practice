#
# Write a function that takes a list of numbers and returns the sum of their squares. Example: sum_of_squares([1, 2, 3]) should return 14.
def sum_of_squares(my_list):
    """
    Calculates the sum of squares of all numbers in the input list.

    Args:
        my_list (list): A list of numbers.

    Returns:
        int: The sum of squares of all numbers.
    """
    return sum(number ** 2 for number in my_list)

result = sum_of_squares([1, 2, 3])
print(result)
