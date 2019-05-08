from collections import Counter


# done in 20 minutes
def checkio(data: list) -> list:
    counted = Counter(data)
    uniq = []
    for k, v in counted.items():
        if v == 1:
            uniq.append(k)

    new_list = []
    for x in data:
        if x not in uniq:
            new_list.append(x)

    return new_list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
