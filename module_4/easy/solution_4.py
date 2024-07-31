#
# Write a function that takes a list of numbers and returns a list with each value doubled. Example: double_values([1, 2, 3]) should return [2, 4, 6].
def double_values(values):
    """
    Returns a new list containing the doubled values of the input list.

    Args:
        values (list): A list of numbers to be doubled.

    Returns:
        list: A new list containing the doubled values.
    """
    return [value * 2 for value in values]

numbers = [9, 6, 3]
result = double_values(numbers)
print(result)
