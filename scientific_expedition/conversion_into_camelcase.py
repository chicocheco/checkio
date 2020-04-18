def to_camel_case(name):
    result = ''
    camel = False
    for i in name:
        if i == '_':
            camel = True
        elif camel:
            result += i.upper()
            camel = False
        else:
            result += i
    return result[0].upper() + result[1:]


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
