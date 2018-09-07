
# done in 5 minutes
# note: second argument of the function int() is by default 10, then it returns the same number until it's not 10
# https://en.wikipedia.org/wiki/Radix
def checkio(str_number: str, radix: int) -> int:
    try:
        return int(str_number, radix)
    except ValueError:
        return -1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
