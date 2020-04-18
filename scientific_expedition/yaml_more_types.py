def yaml(a):
    to_dict = {k: v for k, v in
               sorted((i.split(': ') if ': ' in i else [i[:-1], None] for i in a.split('\n') if i),
                      key=lambda x: x[0])}
    for k, v in to_dict.items():
        if v:
            if v.isdigit():
                v = int(v)
            else:
                v = ' '.join(i.replace('\\"', '"') if '\\"' in i else i for i in v.split())
                if v.endswith('""') or v.startswith('""'):  # because .strip() removes "" at once
                    v = v[1:-1]
                elif v == 'false':
                    v = False
                elif v == 'null':
                    v = None
                else:
                    v = v.strip('"')
        to_dict[k] = v
    return to_dict


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
