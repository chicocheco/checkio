# done in 1 hour
# for next time: if first marker doesn't exist, no need to do anything, because from_index = 0. if second marker is
# missing then len() gives me conveniently the index for the second digit when slicing.


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    len_begin = len(begin)
    len_end = len(end)

    from_index = 0
    to_index = 0

    if end not in text:
        to_index = len(text)

    for index, char in enumerate(text):
        chunk_begin = text[index:index + len_begin]
        chunk_end = text[index:index + len_end]
        if chunk_begin == begin:
            from_index = index + len_begin
        elif chunk_end == end:
            to_index = index

    return text[from_index:to_index]


if __name__ == '__main__':
    # print('Example:')
    # print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
