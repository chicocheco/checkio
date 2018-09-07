# done in 30 minutes
# string.find(symbol) or .index(symbol) return an index just of the FIRST character!! enumerate solves this
def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    if symbol not in text:
        return None

    first_passed = False
    for index, char in enumerate(text):
        if char == symbol and first_passed is False:
            first_passed = True
        elif char == symbol and first_passed is True:
            return index


if __name__ == '__main__':
    # print('Example:')
    # print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
