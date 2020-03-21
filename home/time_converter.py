
def time_converter(time: str) -> str:
    convert = {'13': '1', '14': '2', '15': '3', '16': '4', '17': '5', '18': '6', '19': '7', '20': '8', '21': '9',
               '22': '10', '23': '11', '24': '12'}

    # remove leading zeros
    if time.startswith('0'):
        hours = time[1:2]
    else:
        hours = time[:2]

    # decide whether it's AM or PM
    if int(hours) < 12:
        minutes = f'{time[2:]} a.m.'
        if hours == '0':
            hours = '12'
    else:
        if hours == '12':
            pass
        else:
            hours = convert[hours]
        minutes = f'{time[2:]} p.m.'
    return hours + minutes


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # these "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
