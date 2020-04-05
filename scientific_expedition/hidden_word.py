# COULD NOT SOLVE ON MY OWN
def checkio(text, word):
    w = len(word)
    text = text.replace(' ', '').split('\n')  # split by lines
    # when the word is in horizontal direction (by rows)
    for x in range(len(text)):
        for y in range(len(text[x]) - w + 1):  # the whole word must fit in the line
            # print(f'is the word {word} == {text[x][y:y + w]}')
            if text[x][y:y + w].lower() == word:
                # print('yeah it is!!')
                return [x + 1, y + 1, x + 1, y + w]

    # when the word is in vertical direction (by columns)
    for x in range(len(text) - w + 1):  # the whole word must fit in the column (x = first letter of the word)
        for y in range(len(text[x])):
            try:
                # print(f'checking line {x} and column {y}')
                if ''.join([line[y] for line in text[x:x + w]]).lower() == word:
                    # build a string moving by rows at maximum length of the word
                    # while moving by letters of each row
                    return [x + 1, y + 1, x + w, y + 1]
            except BaseException:  # when the column cannot be completed like ['n', 'o', 'e', ???] at column n. 24
                continue


if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
