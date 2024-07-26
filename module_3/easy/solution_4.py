#
# Write a function count_vowels(string) that returns the number of vowels in the given string.
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

result = count_vowels("Hello WORLD")
print(result)
