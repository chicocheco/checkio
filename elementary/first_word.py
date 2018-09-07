# done in 1 hour

# check only the first character if it's an alphabet, because "'" is not, for example


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    lst = text.split()
    result_string = ''
    for word in lst:
        if word[0].isalpha():
            result_string = word.strip(',')
            break

    if '.' in result_string:
        fixed = result_string.split('.')
        result_string = fixed[0]

    return result_string


if __name__ == '__main__':
    # print("Example:")
    # print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
