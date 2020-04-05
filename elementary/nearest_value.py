import bisect


def nearest_value(values: set, one: int) -> int:
    sort = sorted(values)  # convert to a sorted list
    if one > max(sort):
        return sort[-1]
    # find both neighbouring values
    left = one - sort[bisect.bisect(sort, one) - 1]
    right = sort[bisect.bisect(sort, one)] - one
    if right < left or left < 0:
        result = sort[bisect.bisect(sort, one)]
        return result  # right-handed is closer
    else:
        result = sort[bisect.bisect(sort, one) - 1]
        return result  # left-handed is closer


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
