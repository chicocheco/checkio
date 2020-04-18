def letter_queue(commands):
    result = []
    for comm in commands:
        if comm.startswith('POP'):
            if result:
                del result[0]
        elif comm.startswith('PUSH'):
            result.append(comm[-1])

    return ''.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
