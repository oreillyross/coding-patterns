def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  feasible_index = -1
  while left <= right:
    mid = (left + right) // 2
    if feasible(mid):
      feasible_index = mid
      right = mid - 1
    else:
      left = mid + 1
  return feasible_index
