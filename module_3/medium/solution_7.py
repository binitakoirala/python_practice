#
# Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit and returns the result.
def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature in Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return(fahrenheit)

celsius = 20
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C equals to {fahrenheit}°F.")
