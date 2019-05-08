import re

digits = re.compile('\d')
lower_case = re.compile('[a-z]')
upper_case = re.compile('[A-Z]')


# done in 2.5 hours
def checkio(password: str) -> bool:
    if len(password) < 10 or len(password) > 64:
        return False

    if not digits.search(password):
        return False
    if not lower_case.search(password):
        return False
    if not upper_case.search(password):
        return False

    # True + False returns False!
    return True


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('ULFFunH8ni') == True, "7th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. 
In the results you will see the converted results.
"""