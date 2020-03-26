VOWELS = "aeiouy"

"""
    - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
"""


def translate(phrase):
    # my own solution (few hours...)
    result = []
    vowels_row = []
    random_vowel = False
    for letter in phrase:
        if len(vowels_row) == 2:  # apply second rule - every time a vowel gets repeated 3x, keep only 1 from these 3
            result.append(vowels_row[0])
            vowels_row = []
        elif letter not in VOWELS:
            result.append(letter)
            if letter != ' ':
                random_vowel = True  # apply first rule - skip 1 random vowel after consonant
        elif random_vowel:
            random_vowel = False
        else:
            vowels_row.append(letter)

    return ''.join(result)


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(translate("aaa bo cy da eee fe"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
