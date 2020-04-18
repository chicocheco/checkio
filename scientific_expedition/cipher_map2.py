def recall_password(cipher_grille, ciphered_password):
    result = []
    indices_x = []
    for i in range(4):
        for row, _ in enumerate(cipher_grille):  # better way of looping over indices than range(len(cipher_grille))
            for column, _ in enumerate(cipher_grille):
                if cipher_grille[row][column] == 'X':
                    indices_x.append((row, column))
        for row, _ in enumerate(ciphered_password):
            for column, _ in enumerate(ciphered_password):
                if (row, column) in indices_x:
                    result.append(ciphered_password[row][column])
        cipher_grille = tuple(i for i in zip(*cipher_grille[::-1]))  # rotate 90deg. clockwise
        indices_x.clear()
    return ''.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
