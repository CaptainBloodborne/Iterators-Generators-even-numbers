### Generators/Iterators module, find even numbers task
***
#### Description

You need to find all even numbers in the following list structure:

        [
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
            [[28, 29, 30], [31, 32, 33], [34, 35, 36]]
        ]

You should implement the algorithm using the following ways:
- function which returns `List[int]` -> `get_even_for_loop`
- function which returns `Generator` -> `get_even_for_loop_iterator`
- function which returns `List[int]`but implemented using list comprehension -> `get_even_list_comprehension`

#### Example


    >>> VALUES = [
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
        [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
        [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    ]
    >>> print(get_even_for_loop(VALUES))
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    >>> print(list(get_even_for_loop_iterator(VALUES)))
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    >>> print(get_even_list_comprehension(VALUES))
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

        