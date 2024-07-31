#
# Write a function that maps a function to a list, but only to elements that satisfy a condition. Example: map_with_condition([1, 2, 3, 4], lambda x: x * 2, lambda x: x % 2 == 0) should return [2, 4].
def map_with_condition(lst, condition):
    """
    Filters a list based on a given condition.

    Args:
        lst (list): The input list to be filtered.
        condition (function): A function that takes an element of the list as input and returns a boolean value.

    Returns:
        list: A new list containing only the elements from the input list that satisfy the given condition.
    """
    satisfied = [x for x in lst if condition(x)]
    return satisfied

lst = [1, 2, 3, 4]
result = map_with_condition(lst, lambda x: x % 2 == 0)
print(result)
