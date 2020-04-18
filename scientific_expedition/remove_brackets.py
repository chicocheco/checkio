"""
If there are more than one correct answer, then you should choose the one where the character that can be removed is
closer to the beginning. For example, in this case "[(])", the correct answer will be "()",
since the removable brackets are closer to the beginning of the line.
"""


# COULD NOT SOLVE ON MY OWN
def remove_brackets(string):
    possible_pairs = []
    for i in range(len(string)):  # get access to left
        for j in range(len(string)):  # get access to right
            if string[i] + string[j] in '()[]{}' and i < j:  # now concatenate and do membership test
                possible_pairs.append((i, j))

    """
    nearest brackets first if same distance, let's remove the first one, so keep the first from end
    in other words if there are two or more pairs of the same distance, order these by the first index descending
    [(0, 2), (0, 4), (1, 2), (1, 4), (3, 4)] -> difference between 3,4 and 1,2 is 1 
    [(3, 4), (1, 2), (0, 2), (1, 4), (0, 4)] -> but we want to give the priority
    and to do that we compare the first index of a pair but in descending order so that would be -3 and -1 so (3, 4)
    goes first
    """
    possible_pairs.sort(key=lambda pair: (pair[1] - pair[0], -pair[0]))
    print(possible_pairs)

    # list of indices to keep and list of indices that are in between, so no longer available to make matching pairs
    indices_to_keep = set()
    # to prevent creating overlaps like [(]) and we already prioritize () over [] thanks to "-pair[0]" rule (see above)
    consumed_indices = set()

    for pair in possible_pairs:
        if pair[0] not in consumed_indices and pair[1] not in consumed_indices:
            # this pair is valid, let's track that
            indices_to_keep |= set(pair)  # union operator (unify two sets), convert the tuple to a set first
            # all indices in between as well as x,y are now consumed
            consumed_indices |= set(range(pair[0], pair[1] + 1))

    # print(''.join(string[i] for i in range(len(string)) if i in indices_to_keep))
    return ''.join(string[i] for i in range(len(string)) if i in indices_to_keep)


if __name__ == '__main__':
    # print("Example:")
    # print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing

    assert remove_brackets('(()()') == '()()'
    # assert remove_brackets('[][[[') == '[]'
    # assert remove_brackets('[[(}]]') == '[[]]'
    # assert remove_brackets('[[{}()]]') == '[[{}()]]'
    # assert remove_brackets('[[[[[[') == ''
    # assert remove_brackets('[[[[}') == ''
    # assert remove_brackets('') == ''
    # assert remove_brackets('[(])') == '()'
    # assert remove_brackets('[(()]') == '[()]'
    # print("Coding complete? Click 'Check' to earn cool rewards!")
