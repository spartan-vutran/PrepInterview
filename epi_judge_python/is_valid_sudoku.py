from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    nullValue = 0
    length = len(partial_assignment)
    for i in range(0, length):
      for j in range(0, length):
        if partial_assignment[i][j] != nullValue:
          for k in range(0, length):
            if k != j and partial_assignment[i][j] == partial_assignment[i][k]:
               return False
          for k in range(0, length):
             if k != i and partial_assignment[i][j] == partial_assignment[k][j]:
               return False
          rowSubSqr = int(i/3)
          colSubSqr = int(j/3)
          for k in range(3*rowSubSqr, 3*(rowSubSqr+1)):
            for m in range(3*colSubSqr, 3*(colSubSqr+1)):
              if k!=i and m!=j and partial_assignment[i][j] == partial_assignment[k][m]:
                return False
    
    return True

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
