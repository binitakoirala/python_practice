#
# Write a function that takes a list of lists and returns a flattened list. Example: flatten([[1, 2], [3, 4]]) should return [1, 2, 3, 4].
def flatten_list(my_list):
    """
    This function takes a list of lists as an argument and returns a single flat list.
    
    Args:
        my_list (list): A list of lists.
    
    Returns:
        list: A single flat list containing all elements from the nested list.
    """
    flat_list = []
    for sublist in my_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

my_list = [[1, 2], [3, 4]]
flattened_list = flatten_list(my_list)
print(flattened_list)
