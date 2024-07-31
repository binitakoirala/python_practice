#
# Write a function that takes a list of strings and returns only those that are palindromes. Example: filter_palindromes(["racecar", "hello"]) should return ["racecar"].
def is_palindrome(string):
    """
    Filter a list of strings to include only those that are palindromes.

    Args:
        string and string_list (list of string): A list of strings to filter.

    Returns:
        list of string: A new list containing only the strings from the input list that are
    """
    return string == string[::-1]

def filter_palindromes(string_list):
    return [string for string in string_list if is_palindrome(string)]

result = filter_palindromes(["racecar", "hello"])
print(result)
