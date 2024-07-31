#
# Write a function that takes a list of words and returns a dictionary grouping the words by their length. Example: group_by_length(["hi", "hello", "cat"]) should return {2: ["hi"], 5: ["hello"], 3: ["cat"]}.
def group_by_length(words):
    """
    Returns a dictionary grouping words by length.

    Args:
        words (list): A list of words to be grouped by length.

    Returns:
        dict: A dictionary where the keys are the length of the word and the values are lists if words of that length.
    """
    word_length = {}
    for word in words:
        length = len(word)
        if length not in word_length:
            word_length[length] = []
        word_length[length].append(word)
    return word_length

result = group_by_length(["hi", "hello", "cat"])
print(result)
