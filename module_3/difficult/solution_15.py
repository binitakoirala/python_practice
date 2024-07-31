#
# Write a function draw_shape(shape, size, char="*") that draws a given shape (like a square or triangle) using an optional character. The shape type can be "square" or "triangle".
def draw_shape(shape, size, char="*"):
    """
    Draws a shape of a specified size using a specified character.

    Args:
        shape (str): The type of shape to draw.
        size (int): The size of the shape to draw.
        char (str, optional): The character to use when drawing the shape. Defaults to "*".

    Returns:
        None
    """
    for i in range(size):
        if shape == "square":
            print(size * char)

        elif shape == "triangle":
            print()

draw_shape("square" , 3)
