#
# Write a function calculate_price(price, tax_rate=0.05) that returns the total price including tax. If no tax rate is provided, it defaults to 5%.
def calculate_price(price, tax_rate=0.05):
    """
    Calculates the total price of an item including tax.

    Args:
        price (float): The base price of the item.
        tax_rate (float, optional): The tax rate as a decimal. Defaults to 0.05.

    Returns:
        float: The total price of the item including tax.
    """
    return price + (price * tax_rate)

print(calculate_price(500))
