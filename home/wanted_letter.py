"""
1. casing does not matter - done via .lower()
2. do not count punctuation symbols, digits, whitespaces.. - done via regex
3. if you have two or more letters with the same frequency, then return the letter which comes first in the alphabet

"""

import re
from collections import Counter

clean = re.compile('[a-z]')


def checkio(text: str) -> str:
    count = dict(Counter(text.lower()).most_common())

    count_cleaned = {}
    for k, v in count.items():
        if clean.search(k):
            count_cleaned[k] = v

    most_freq_letters = {}
    for key, value in count_cleaned.items():
        if value == max(count_cleaned.values()):
            most_freq_letters[key] = value

    most_freq_letters_cleaned = sorted(most_freq_letters.keys())
    result = most_freq_letters_cleaned[0]
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
