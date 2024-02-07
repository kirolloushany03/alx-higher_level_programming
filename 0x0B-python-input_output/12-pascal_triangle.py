#!/usr/bin/python3
'''pascals triangle module'''


def pascal_triangle(n):

    '''
    Generates a list of lists representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's.

    Returns:
        list(list(int)): A list of lists representing the Pascal's triangle
    '''

    if n <= 0:
        return []
    triangle = [[1]]
    '''Initialize the triangle with first row'''
    for i in range(1, n):
        previous_row = triangle[-1]
        '''Get previous row'''
        current_row = [1]
        '''Initialize current row with 1'''
        for j in range(1, len(previous_row)):
            current_row.append(previous_row[j-1] + previous_row[j])
            ''' Add sum of previous adjacent elements'''
        current_row.append(1)
        '''Add 1 to the end of the current row'''
        triangle.append(current_row)
        '''Append the current row to the triangle'''
    return triangle
