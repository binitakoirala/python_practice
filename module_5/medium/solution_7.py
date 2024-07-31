#
# Write a function that takes a list and returns only the elements that appear exactly once. Example: filter_unique([1, 2, 2, 3, 4, 4]) should return [1, 3].
def filter_unique(lst):
    """
    Returns a new list containing only the elements that appear exactly once in the input list.

    Args:
        lst (list): The input list to be filtered.

    Returns:
        list: A new list containing only the unique elements from the input list.
    """
    filtered_list = []
    for element in lst:
        if lst.count(element) == 1:
            filtered_list.append(element)
    return filtered_list

lst = [1, 2, 2, 3, 4, 4]
print(filter_unique(lst))
