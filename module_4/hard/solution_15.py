#
# Write a function that counts the frequency of each word in a list. Example: word_frequencies(["apple", "banana", "apple"]) should return {"apple": 2, "banana": 1}.
def word_frequencies(words):
    """
    Returns a dictionary with the frequency of each word in the list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words as keys and their count as values. 
    """
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

words = ["apple", "banana", "apple"]
print(word_frequencies(words))
