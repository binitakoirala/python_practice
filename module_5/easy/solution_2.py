#
# Write a function that takes a list of numbers and returns a list of cumulative sums. Example: cumulative_sum([1, 2, 3]) should return [1, 3, 6].
def cumulative_sum(numbers):
    """
    Calculate the cumulative sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of cumulative sums, where each element is the sum of all numbers up to that point in the input list.
    """
    cumulative_sums = []
    sum = 0    
    for number in numbers:
        sum += number
        cumulative_sums.append(sum)
    return cumulative_sums

numbers = [1, 2, 3]
print(cumulative_sum(numbers))
