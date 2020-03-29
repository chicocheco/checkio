def split_list(items: list) -> list:
    # your code here
    if len(items) % 2 == 0:
        split_by = int(len(items) / 2)
    else:
        split_by = len(items) - int(len(items) // 2)
    return [items[0:split_by], items[split_by:]]


if __name__ == '__main__':
    # print("Example:")
    # print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
