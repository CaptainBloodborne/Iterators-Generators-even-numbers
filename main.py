from typing import Generator, List

VALUES = [
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
]


def get_even_for_loop(values: List) -> List[int]:
    """Return all even numbers using classical for loop.
    :param values: input list of lists with values
    :return: list with int values
    """
    even_list = []
    for outer_list in values:
        for inner_list in outer_list:
            for value in inner_list:
                if value % 2 == 0:
                    even_list.append(value)
    return even_list


def get_even_for_loop_iterator(values: List) -> Generator:
    """Return all even numbers using generator.
    :param values: input list of lists with values
    :return: generator with int values
    """
    return (
        value
        for outer_list in values
        for inner_list in outer_list
        for value in inner_list
        if value % 2 == 0
    )


def get_even_list_comprehension(values: List) -> List[int]:
    """Return all even numbers in ONE LINE using list comprehension.
    :param values: input list of lists with values
    :return: list with int values
    """

    return [
        value
        for outer_list in values
        for inner_list in outer_list
        for value in inner_list
        if value % 2 == 0
    ]
