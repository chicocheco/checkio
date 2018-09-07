

# done in 10 minutes
# next time: string.replace(old, new) create a copy of the string, doesn't change it in place !!!
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    joined = ','.join(phrases)
    if 'right' in joined:
        replaced = joined.replace('right', 'left')  # .replace creates a COPY! need to assign to another variable
        return replaced

    return joined


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
