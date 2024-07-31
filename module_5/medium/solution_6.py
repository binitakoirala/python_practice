#
# Write a function that takes a 2D list (matrix) and returns its transpose. Example: transpose([[1, 2, 3], [4, 5, 6]]) should return [[1, 4], [2, 5], [3, 6]].
def transpose(matrix_list):
    """
    Transpose a given matrix.

    Args:
        matrix_list (list of lists): A 2D list representing the matrix to be transposed.

    Returns:
        list of lists: The transposed matrix.
    """
    return list(map(list, zip(*matrix_list)))
    
matrix_list = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix_list))
