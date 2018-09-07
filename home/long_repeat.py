"""
the algo explained:
1. check that the first character is not None (!= None) and if not, the longest substring is then 0 + 1
2. check that the current character is not the same as the last one which is not None anymore because now it's set to
the first character of the string and check what is the maximum length of repeating characters so far and save it to
 the variable "longest_len" and also if they are not the same, reset current length to 0
3. if the last character is the same as the current one, increase "current" by 1
4. return the maximum value from variables longest_len and current_len

"""


# took me the ***king entire day
# NOTE FOR THE NEXT TIME: Never forget to consider the max() function instead of operators like > < etc.
def long_repeat(line):
    # this is the best solution, but not mine
    last = None
    longest_len = 0
    current_len = 0
    for c in line:
        if c != last:
            longest_len = max(longest_len, current_len)
            current_len = 0
            last = c
        current_len += 1
    return max(longest_len, current_len)

    # longest_substring = 0
    # counter = 1
    #
    # if line == '':
    #     return 0
    # elif len(line) == 2 and line[0] == line[1]:
    #     return 2
    #
    # for i in range(len(line) - 1):
    #     if line[i] == line[i + 1]:
    #         counter += 1
    #     elif counter > longest_substring:
    #         longest_substring = counter
    #     else:
    #         counter = 1
    #
    # return longest_substring




# long_repeat('sdsffffse')
# long_repeat('ddvvrwwwrggg')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
