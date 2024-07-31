#
# Write a function that checks if two strings are anagrams of each other. Example: is_anagram("listen", "silent") should return True.
def is_anagram(string1, string2):
    """
    Checks if two input strings are anagrams of each other.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        bool: True if the input strings are anagrams, False otherwise.
    """
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    return sorted(string1) == sorted(string2)

result = is_anagram("listen", "silent")
print(result)
