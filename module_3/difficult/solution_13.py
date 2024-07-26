#
# Write a function validate_email(email) that returns True if the given email is valid and False otherwise.
import re

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-z]{2,}$"
    if re.match(email_regex, email):
        return True
    return False

print(validate_email("@binitagmail.com"))
