#
# Write a function send_email(to, subject="No Subject") that sends an email. For this challenge, simply return a formatted string stating the email was sent.
def send_email(to, subject="No Subject"):
    """
    Sends an email to the specified recipient with the given subject.

    Args:
        to (str): The address of the recipient.
        subject (str, optional): The subject of the email. Defaults to "No Subject".

    Returns:
        str: A formatted string stating that the email was sent.
    """
    return (f"The email with subject {subject} has been sent to {to}.")

print(send_email("Binita"))
