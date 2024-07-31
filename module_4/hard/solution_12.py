#
# Write a function that returns the product of all numbers in a list. Example: product_of_list([1, 2, 3]) should return 6.
def product_of_list(numbers):
    """
    Calculate the product of all numbers in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The product of all numbers in the list.
    """
    product = 1
    for number in numbers:
        product *= number
    return product

number_list = [1, 2, 3]
result = product_of_list(number_list)
print(result)
