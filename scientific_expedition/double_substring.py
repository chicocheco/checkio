from collections import deque, Counter


def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """

    """
    1. is 'ag' in 'htfghkofgh'? slice 0:2, slice 2:, no
    2. is 'gh' in 'tfghkofgh'? slice 1:3, 3:, yes
    3. is 'ht' in 'fghkofgh'? slice 2:4, 4:, no
    4. is 'tf' in 'ghkofgh'?
    5. is 'fg' in 'hkofgh'?
    6. is 'gh' in 'kofgh'?
    7. is 'hk' in 'ofgh'?
    8. is 'ko' in 'fgh'?
    9. is 'of' in 'gh'?
    
    is 'agh' in 'tfghkofgh'? slice 0:3, slice 2:, no
    is 'ght' in 'fghkofgh'? slice 1:4, slice 3:, no
    is 'htf' in 'ghkofgh'? slice 2:5, slice 4:, no
    is 'tfg' in 'hkofgh'? slice 3:6, slice 5:, no
    is 'fgh' in 'kofgh'? - slice 4:7, slice 4:, yes!
    
    
    """
    # my own solution that took only some hours to come up with...
    lst = list(line)
    match = []
    for y in range(1, len(line)):
        rest = deque(lst[y:])  # shorten the string from left
        for i in range(len(line)):
            sub = line[i:i + y]  # search the string for substring of expanding length
            rest_string = ''.join(rest)
            if sub in rest_string:
                match.append(sub)
            if rest:
                rest.popleft()
    return max([len(i) for i in match], default=0)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # double_substring('aghtfghkofgh')

    assert double_substring('aaaa') == 2, "aa"
    assert double_substring('abcab') == 2, "ab"
    assert double_substring('abc') == 0, "abc"
    assert double_substring('aghtfghkofgh') == 3, "fgh"
    assert double_substring('abababaab') == 3, "aba"
    print('"Run" is good. How is "Check"?')
