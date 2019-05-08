def is_stressful(subj):
    red_words = ['help', 'asap', 'urgent']
    if subj.isupper():
        return True
    elif subj[-3:] == '!!!':
        return True
    else:
        split_subj = subj.split()

        for word in split_subj:
            clean = ''
            last_char = ''
            for char in word:

                if char.isalpha() and char.lower() != last_char:
                    clean += char.lower()
                last_char = char.lower()
            print(clean)
            if clean in red_words:
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    assert is_stressful("UUUURGGGEEEEENT here") is True, "Third"
    assert is_stressful("We need you A.S.A.P.!!") is True, "Forth"
    print('Done! Go Check it!')

    """The function should recognise if a subject line is stressful. A stressful subject line means that all letters 
    are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” 
    words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", 
    "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP" """
