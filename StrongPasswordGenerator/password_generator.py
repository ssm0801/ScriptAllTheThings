"""
Strong Password Generator

- Generates a secure random password of 12 digits using the secrets module (much better than random!) and the string module

Author: Skyascii (https://github.com/savioxavier)
Date: 1/10/2021
"""

import secrets
import string


def generate_password(length=12):
    """Generates a random password

    Args:
        length (int, optional): Length of the generated password. Defaults to 12.

    Returns:
        str: The output generated password
    """
    req_str = string.ascii_letters + string.digits

    secure_pass = "".join((secrets.choice(req_str) for i in range(length)))

    return secure_pass


print(f"Your password: {generate_password(12)}")
