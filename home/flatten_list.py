def flat_list(array):
    # lst_flat = []
    # # TODO: my solution works only 3 levels deep
    # for element in array:
    #     if type(element) == list:
    #         for sub_element in element:
    #             if type(sub_element) != list:
    #                 lst_flat.append(sub_element)
    #             else:
    #                 for x in sub_element:
    #                     lst_flat.append(x)
    #     else:
    #         lst_flat.append(element)
    # return lst_flat

    # not my solution:
    for i, x in enumerate(array):
        while i < len(array) and isinstance(array[i], list):
            # so for example we take an element (a sublist) at index 1 like array[1] and we assign it as a slice 1:2
            # this will preserve strings, integers and so on and "unpack" iterables
            array[i:i + 1] = array[i]
    return array


# flat_list([1, 2, 3])
# flat_list([1, [2, 2, 2], 4])
# flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
# flat_list([-1, [1, [-2], 1], -1])

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
