import string


def check_pangram(text):
    for i in string.ascii_lowercase:
        if i not in text.lower():
            return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    assert not check_pangram(
        "!F]gatv]FZ;.MVl=wGC%nr*$np#'bn?}oIOa_YMf]MBQpB^Ndh_T/hw^D*hxcZVUp-ugO<nfC,N@:ag?TMby:A^*?qV_BK")
    print('If it is done - it is Done. Go Check is NOW!')
