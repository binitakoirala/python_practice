#
# Write a function that takes a list of names and returns a list with each name capitalized. Example: capitalize_names(["alice", "bob"]) should return ["Alice", "Bob"].
def capitalize_names(names):
    """
    Capitalize the first letter of each name in a list of names.

    Args:
        names (list): A list of names as stringd.

    Returns:
        list: A list of names with the first letter of each name capitalized.
    """
    capitalized_name = [name.title() for name in names]
    return capitalized_name

names = ["binita", "koirala"]
result = capitalize_names(names)
print(result)
