#
# Write a function that merges two lists into a list of tuples, pairing elements with the same index. Example: merge_lists([1, 2], ["a", "b"]) should return [(1, "a"), (2, "b")].
def merge_lists(list1, list2):
    """
     Merge two lists into a list of tuples, where each tuple contains one element from each list.

    Args:
        list1 (list): The first list to merge.
        list2 (list): The second list to merge.

    Returns:
        list: A list of tuples, where each tuple contains one element from list1 and one element from list2.
    """
    merged_list = list(zip(list1, list2))
    return merged_list

list1 = [1, 2]
list2 = ["a", "b"]

print(merge_lists(list1, list2))
