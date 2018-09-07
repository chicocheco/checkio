

# done in 40 minutes
# note: learn how to do these algos, similar to "long_repeat.py"
def checkio(words: str) -> bool:
    current = longest = 0  # the same as separately current = 0 and longest = 0
    for element in words.split():
        if element.isalpha():
            current += 1
            longest = max(longest, current)  # before I reset it to zero, I have to record the maximum!
        else:
            current = 0

    print(current, longest)

    if longest > 2:
        return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
