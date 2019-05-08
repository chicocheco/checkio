"""
For white pawns the front squares are squares with greater row number than the square they currently occupy.
A pawn is safe if another pawn can capture a unit on that square.

1. Pawns can move forward ONLY (from row 1 to higher)
2. I'm checking the cell, where the pawn is, meaning that if I can capture a unit which is put in that cell,
the cell is protected, the pawn there is protected too.
3. Look at the pawns, point at each and ask yourself "could an enemy's unit be captured by another pawn if it were
in this particular cell?" If the answer is YES = the unit in there is safe!!
"""


# done in 3 hours
# note for next time: no need to compare something to something if you can check only if it exists!!
def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()

    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))

    count = 0
    for row, col in pawns_indexes:
        # check for pawns diagonally but only behind and even 1 is enough to protect
        if ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes):
            count += 1

    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
