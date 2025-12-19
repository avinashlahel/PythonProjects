import string
import secrets


def hasUpperCase(str):
    for w in str:
        if w in string.ascii_uppercase:
            return True

    return False

def hasSymbol(str):
    for w in str:
        if w in string.punctuation:
            return True

    return False

"""
Generates password
"""
def generate_password(length: int, upper: bool, symbol: bool):
    if length < 2:
        return "Length cannot be less than 2"

    combination: str = string.ascii_lowercase

    if upper:
        combination += string.ascii_uppercase
    if symbol:
        combination += string.punctuation

    newpass = ''
    comblength = len(combination)

    for _ in range(length):
        newpass += combination[secrets.randbelow(comblength)]

    if hasSymbol(newpass) and hasUpperCase(newpass):
        return newpass


    return generate_password(length, upper, symbol)



if __name__ == '__main__':
    print(generate_password(10, True, True))