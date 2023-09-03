from typing import List, Tuple

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.

def medium5(A: List, left:int, right:int) -> int:
  if right == left:
    return left
  if right < left:
    return - 1

  isSorted = False
  while not isSorted:
    i = left
    isSorted = True
    while i < right:
      if A[i] > A[i+1]:
        isSorted = False
        A[i], A[i+1] = A[i+1], A[i]
      i = i+1
  mid = int((right-left)/2 + left)
  return mid



def pivot1(A: List, left:int, right:int) -> int:
  if right - left + 1 <= 5:
    return medium5(A, left, right)

  # Find med5 of sub array of length 5
  for i in range(left, right+1, 5):
    if i + 4 > right: 
      subRight = right
    else:
      subRight =  left + 4

    mediumI = medium5(A, i, subRight)
    groupTh = int(i/5)
    A[groupTh], A[mediumI] = A[mediumI],  A[groupTh]

  mid = int((right-left+1)/10) + left + 1
  return select(A, left, int((right-left)/5), mid)


def partition(A: List, pivot: int, left:int, right:int) -> Tuple[int]:
  # [6, 5, 7, 8]
  eI, gI = left, left+1
  A[pivot], A[left] = A[left], A[pivot]
  pivot = A[left]
  kTh = 1
  for i in range(left+1, right+1):
    if A[i] <= pivot:
      A[i], A[gI] = A[gI], A[i]
      gI += 1
      if A[gI-1] < pivot:
        A[gI-1], A[eI] = A[eI], A[gI-1]
        eI += 1
      continue
    kTh += 1
  return (kTh, eI, gI)
  

def select(A: List, left: int, right: int, k:int) -> int:
  # [2, 5, 3, 3, 6, 7 ,8]
  # [2,3,3,6,5] 
  if k <=0 or k > (right-left+1):
    return -1

  while True:
    pivot = pivot1(A, left, right)
    kTh, kThI, nextkThI = partition(A, pivot, left, right)
    if kTh == k:
      return kThI
    elif kTh < k:
      right = kThI - 1
      k = k - kTh
    else:
      left = nextkThI


def find_kth_largest(k: int, A: List[int]) -> int:
  # TODO - you fill in here.
  resultIndex = select(A, 0, len(A) - 1, k)
  return A[resultIndex]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
