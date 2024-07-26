#
# Write a function is_palindrome(string) that checks if a given string s is a palindrome and returns True or False.
def is_palindrome(string):
    """
    Checks if a given string is a palindrome.

    Args:
        string: The input string to be checked.

    Returns:
        bool: True if a string is a palindrome, False otherwise.
    """
    return string == string[::-1]

word = "SOS"

if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
