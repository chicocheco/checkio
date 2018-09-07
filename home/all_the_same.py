from typing import List, Any


# done in 10 minutes
def all_the_same(elements: List[Any]) -> bool:
    # your code here
    print(len(set(elements)))
    if not elements:
        return True
    elif len(set(elements)) != 1:
        return False

    return True


if __name__ == '__main__':
    # print("Example:")
    # print(all_the_same([1, 1, 1]))
    # print(all_the_same([1, 2, 1]))
    # print(all_the_same(['a', 'a', 'a']))
    # print(all_the_same([]))
    # print(all_the_same([1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
