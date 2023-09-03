from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    length = len(square_matrix)
    i = 0
    result = [] 
    while i < int(length/2):
      for c in range(i, length-i-1):
        result.append(square_matrix[i][c])
      for r in range(i, length-i-1):
        result.append(square_matrix[r][length-1-i])
      for c in range(length-1-i, i, -1):
        result.append(square_matrix[length-1-i][c])
      for r in range(length-1-i, i, -1):
        result.append(square_matrix[r][i])
      i += 1
    
    if length % 2 != 0 and length != 0:
      result.append(square_matrix[i][i])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
