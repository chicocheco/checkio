def caps_lock(text: str) -> str:
    caps_active = False
    output = ''
    for char in text:
        if char == 'a':
            if not caps_active:
                caps_active = True
            else:
                caps_active = False
        elif caps_active:
            output += char.upper()
        else:
            output += char
    return output


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
