#
# Write a function that finds all pairs of numbers in a list that sum to a specific target. Example: sum_of_pairs([1, 2, 3, 4], 5) should return [(1, 4), (2, 3)].
def sum_of_pairs(lst, condition):
    """
    Returns a list of pairs of numbers from the list that sum up to the condition.

    Args:
        lst (list): A list of numbers.
        condition (int): The target sum.

    Returns:
        list: A list of tuples, where each tuple contains a pair of numbers from the list that sum up to the condition.
    """
    sum = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == condition:
                sum.append((lst[i], lst[j]))
    return sum

print(sum_of_pairs([1, 2, 3, 4], 5))
