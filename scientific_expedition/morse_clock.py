"""
0	0
1	1
2	10
3	11
4	100
5	101
6	110
7	111
8	1000
9	1001
"""


def checkio(time_string: str) -> str:
    morse = ('....', '...-', '..-.', '..--', '.-..', '.-.-', '.--.', '.---', '-...', '-..-')
    four_slots = {str(k): v for k, v in zip(range(11), morse)}

    hours, minutes, seconds = (i.zfill(2) for i in time_string.split(':'))

    hours = f'{four_slots[hours[0]][2:]} {four_slots[hours[1]]}'
    minutes = f'{four_slots[minutes[0]][1:]} {four_slots[minutes[1]]}'
    seconds = f'{four_slots[seconds[0]][1:]} {four_slots[seconds[1]]}'
    return f'{hours} : {minutes} : {seconds}'


if __name__ == '__main__':
    # print("Example:")
    # print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
