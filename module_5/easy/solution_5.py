#
# Write a function that takes a string and returns a dictionary with the frequency of each letter. Example: letter_frequency("banana") should return {"b": 1, "a": 3, "n": 2}.
def letter_frequency(word):
    """
    Returns the frequency of each letter in a given word.

    Args:
        word (str): The input word.

    Returns:
        dict: A dictionary where the keys are the letters in the word and the values are their respective frequencies.
    """
    letter_count = {}
    for letter in word.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] +=1
            else:
                letter_count[letter] = 1
    return letter_count

word = "banana"
print(letter_frequency(word))
