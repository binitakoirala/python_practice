#
# Write a function that takes a list of words and returns the total count of words. Example: count_words(["hello", "world"]) should return 2.
def count_words(words):
    """
    Counts the total number of words in a given list.

    Args:
        words (list): A list of words.

    Returns:
        int: The total number of words in the list.
    """
    total_words = len(words)
    return total_words

words = ["hello", "world"]
result = count_words(words)
print(result)
