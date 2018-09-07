
# done in 2 hours
# next time: to iterate over digits, convert to string. After variable 'last' gets a value it can be merged with
# the variable 'product' because I'm interested only in the product of the last two number in next iterations.

def checkio(number: int) -> int:
    new_list = [num for num in str(number)]
    last = None
    product = int(new_list[0])
    for num in new_list:
        if not last:
            last = int(num)
            continue
        elif num != '0':
            product = last = last * int(num)

    return product

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
