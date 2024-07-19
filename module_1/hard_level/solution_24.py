#
#  Write a program that asks the user to enter a password and checks if it meets the following criteria:at least 8 characters, contains at least one uppercase letter, one lowercase letter, and one number.

def is_password_valid(password):
    if len(password) >= 8:
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                if any(char.isdigit() for char in password):
                    return True
    else:
        return False
    
password = input('Enter a password: ')

if is_password_valid(password):
    print('Valid Password.')
else:
    print('Invalid Password.')
