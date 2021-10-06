import string

def passwordValidator():
    """
    Validates passwords to match specific rules
    : return: str
    """
    userPassword = input('\nEnter a valid password: ').strip()
   # check if user's password conforms 
   # to the rules above
    if not(6 <= len(userPassword) <= 12):
        message = 'Invalid Password..your password should have a minimum '
        message += 'length of 6 and a maximum length of 12'
        return message
    if ' ' in userPassword:
       message = 'Invalid Password..your password shouldn\'t contain space(s)'
       return message
    if not any(i in string.ascii_letters for i in userPassword):
       message = 'Invalid Password..your password should contain at least '
       message += 'an uppercase letter and a lowercase letter'
       return message
    if not any(i in string.digits for i in userPassword):
        message = 'Invalid Password..your password should contain at least a number'
        return message
    if not any(i in string.punctuation for i in userPassword): 
       message = 'Invalid Password..your password should contain at least a special character'
       return message
    else:
       return 'Valid Password!'

my_password = passwordValidator()
print(my_password)
