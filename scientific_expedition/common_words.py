"""
The result must be represented as a string of words separated by commas in alphabetic order.
"""


def checkio(first, second):
    intersection = set(first.split(',')) & set(second.split(','))
    sort = sorted(list(intersection))
    return ','.join(sort)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print(checkio("one,two,three", "four,five,one,two,six,three"))
    # print(checkio("one,two,three", "four,five,six"))
    # print(checkio("hello,world", "hello,earth"))

    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
