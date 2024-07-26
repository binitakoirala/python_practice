#
# Write a function find_maximum(number_list) that returns the maximum element in a list.
def find_maximum(number_list):
    """
    Finds and returns the maximum value in a given list of numbers.

    Args:
        number_list (list): A list of integers.

    Returns:
        int: The maximum value in the input list.
    """
    return max(number_list)

number = [1, 5, 99, 20, 76]
print(find_maximum(number))
