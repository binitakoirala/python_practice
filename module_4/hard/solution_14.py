#
# Write a function that partitions a list into two lists: one with elements satisfying a condition and one with elements that do not. Example: partition_list([1, 2, 3, 4], lambda x: x % 2 == 0) should return ([2, 4], [1, 3]).
def partition_list(lst, condition):
    """
    Partitions a list into two lists based on a given condition.

    Args:
        lst (list): The input list to be partitioned.
        condition (function): A function that takes an element of the list as input and returns a boolean value.

    Returns:
        tuple: A tuple containing two lists. The first list contains elements from the input list that satisfy the condition,
        and the second list contains elements that do not satisfy the condition.
    """
    satisfied = [x for x in lst if condition(x)]
    not_satisfied = [x for x in lst if not condition(x)]
    return satisfied, not_satisfied

number_list = [1, 2, 3, 4]
result = partition_list(number_list, lambda x: x % 2 ==0)
print(result)
