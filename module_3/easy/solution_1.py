#
# Write a function display_list(list) that takes a list and prints each element on a new line.
list = ["hello", "world"]
def display_list(element_list: list) -> None:
    """
    Prints each element from list in a new line.

    Args:
        element_list (list) : A list of elements to be printed.

    Returns:
        None
    """
    for word in element_list:
        print(word)

display_list(list)
