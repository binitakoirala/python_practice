#
# Write a function check_internet_connectivity() that checks if the machine is connected to the internet and returns True or False.
import socket

def check_internet_connectivity():
  """
  Checks if the machine is connected to the internet.

  Args:
    None

  Returns:
    bool: True if connected to the internet, False otherwise.
  """
  try:
    socket.create_connection(("8.8.8.8", 53))  # Connect to Google's public DNS server
    return True
  except OSError:
    return False

if check_internet_connectivity():
  print("Connected to the Internet!")
else:
  print("No internet connection found.")
