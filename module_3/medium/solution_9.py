#
# Write a function get_python_version() that returns the current Python version being used.
import platform

def get_python_version():
    """
    Returns the current Python version being used.

    Args:
        None.

    Returns:
        str: The current Python version.
    """
    version = platform.python_version()
    return version

version = get_python_version()

print(f"Python Version: {version}")
