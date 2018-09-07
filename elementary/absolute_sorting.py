from operator import itemgetter


# done in 30 minutes
# note: use itemgetter in key argument of sort() or sorted()! use dict and list comprehensions!
def checkio(numbers_array: tuple) -> list:
    lst_tup = {(number, abs(number)) for number in numbers_array}
    sort_lst = [x for x, y in sorted(lst_tup, key=itemgetter(1))]

    return sort_lst


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)


    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
