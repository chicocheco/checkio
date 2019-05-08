from typing import List


# done in 2 hours
def checkio(game_result: List[str]) -> str:
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        if game_result[0][0] != '.':
            return game_result[0][0]

    elif game_result[0][2] == game_result[1][1] == game_result[2][0]:
        if game_result[0][2] != '.':
            return game_result[0][2]

    for row in game_result:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] != '.':
                return row[0]

    for row in zip(*game_result):
        row = ''.join(row)
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] != '.':
                return row[0]

    return 'D'


if __name__ == '__main__':
    # print("Example:")
    # print(checkio(["X.O",
    #                "XX.",
    #                "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
