def yaml(a):
    return {k: int(v) if v.isdigit() else v for k, v in
            sorted((i.split(': ') for i in a.split('\n') if i), key=lambda x: x[0])}


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}

    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
