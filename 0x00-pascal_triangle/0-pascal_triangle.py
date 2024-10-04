#!/usr/bin/python3


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing the Pascal's triangle of n
        - Returns an empty list if n <= 0
        - You can assume n will be always an integer
    '''
    if n <= 0:
        return []

    # List of lists of integer
    pascal_list = [
        [1]
    ]
    for row in range(1, n):
        # Start the list (row of triangle) with 1
        new_row = [1]
        for col in range(1, row):
            new_row.append(pascal_list[row - 1][col - 1] + pascal_list[row - 1][col])

        # End the list (row of triangle) with 1
        new_row.append(1)
        pascal_list.append(new_row)

    return pascal_list
