# COULD NOT SOLVE ON MY OWN
def checkio(string):
    string = ''.join(char for char in string if char in '{}[]()')
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return False if string else True


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("(((1+(1+1))))]") == False
    assert checkio("2+3") == True, "No brackets, no problem"
