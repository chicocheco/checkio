from typing import List


def checkio(data: List[int]) -> [int, float]:
    """notes:
    round(4.5)
    4
    round(5.5)
    6"""
    srt_data = sorted(data)

    # if it is odd:
    if len(srt_data) % 2 != 0:
        return srt_data[int(len(srt_data) / 2)]
    else:
        # make a slice to compute the avg, where list[from_inclusive, to_exclusive]!!
        return sum(srt_data[int((len(srt_data) / 2) - 1):int((len(srt_data) / 2) + 1)]) / 2


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
