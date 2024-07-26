#
# Write a function get_system_info() that returns the operating system name and version.
import platform

def get_system_info():
    """
    Displays information about the operating system.

    Args:
        None

    Returns:
        Tuple: A tuple containing the operating system name and version.
    """
    os_name = platform.system()
    os_version = platform.release()

    return (os_name, os_version)

os_name, os_version = get_system_info()

print(f"Operating System: {os_name}")
print(f"Version: {os_version}")
