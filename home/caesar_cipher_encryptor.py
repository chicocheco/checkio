# done in 30 minutes

import string


def to_encrypt(text, delta):
    en_letters = string.ascii_lowercase
    encrypted = ''
    for char in text:
        if char in en_letters:
            index = en_letters.index(char) + delta
            if index > len(en_letters):
                index = index - len(en_letters)

            encrypted += en_letters[index]

        else:
            encrypted += char

    print(encrypted)
    return encrypted

    # return text


if __name__ == '__main__':
    # print("Example:")
    # print(to_encrypt('abc', 10))
    # to_encrypt("simple text", 16)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
