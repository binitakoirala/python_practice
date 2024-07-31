#
# Write a function that takes two lists and returns a list of common elements. Example: intersect_lists([1, 2, 3], [2, 3, 4]) should return [2, 3].
def intersect_list(list1, list2):
    """
    Returns a list of common elements between two input lists.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list of elements that are common to both input lists.
    """
    return list(set(list1) & set(list2))

list1 = [1, 2, 3]
list2 = [2, 3, 4]
print(intersect_list(list1, list2))
