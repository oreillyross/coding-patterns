def two_pointers_opposite(arr):
  left, right = 0, len(arr) - 1
  while left < right:
    current = process(arr[left], arr[right])
    if condition(arr[left], arr[right]):
      left += 1
    else:
      right -= 1

