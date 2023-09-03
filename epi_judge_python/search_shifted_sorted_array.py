from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
  left, right = 0, len(A) - 1
  while left < right:
    mid = int((right - left)/2) + left
    if (mid + 1 > len(A) or A[mid] < A[mid+1]) and (mid - 1 < 0 or A[mid] < A[mid-1]):
      return mid
    elif A[mid] < A[right]:
      right = mid - 1
    elif A[mid] > A[right]:
      left = mid + 1

  return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
