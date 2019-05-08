from collections import Counter


# done in 30 minutes
# for next time: use dictionary comprehensions!! and just compare two dictionaries!
def popular_words(text: str, words: list) -> dict:
    new_dict = {word: 0 for word in words}

    for key, value in Counter(text.lower().split()).items():
        if key in new_dict.keys():
            new_dict[key] = value

    return new_dict


if __name__ == '__main__':
    #     print("Example:")
    #     print(popular_words('''
    # When I was One
    # I had just begun
    # When I was Two
    # I was nearly new
    # ''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
