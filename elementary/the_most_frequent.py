from collections import Counter


# done in 10 minutes
# note: get the letter using [0][0] from a list of dictionaries
def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    count = Counter(data).most_common(1)[0][0]
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
