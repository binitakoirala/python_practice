#
# Write a function that removes duplicate elements from a list while preserving order. Example: remove_duplicates([1, 2, 2, 3]) should return [1, 2, 3].
from collections import OrderedDict

def remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving the original order.

    Args:
        lst (list): The input list that may contain duplicates.

    Returns:
        list: A list with duplicates removed, preserving the original order of elements.
    """
    unique_list = list(OrderedDict.fromkeys(lst))
    return unique_list

lst = [1, 1, 2, 3]
print(remove_duplicates(lst))
