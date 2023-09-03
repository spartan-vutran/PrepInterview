from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.
    if k==0 or k == 1:
      return k
    
    left, right = 0, k 
    while True:
      mid = int((right- left)/2 + left)
      if mid*mid <= k and (mid+1)*(mid+1) > k:
        return mid

      if mid*mid > k:
        right = mid - 1
      elif mid*mid < k:
        left = mid + 1
    
  


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
