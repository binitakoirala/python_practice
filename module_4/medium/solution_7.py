#
# Write a function that takes a string and returns the number of vowels in it. Example: count_vowels("hello")` should return 2.
def count_vowels(string):
    """
    Returns the number of vowels in the given string.

    Args:
        string (str): The input string to count vowels from.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    return len([char for char in string if char.lower() in vowels])
string = 'hello'
result = count_vowels(string)
print(f"The vowel count in {string} is {result}.")
