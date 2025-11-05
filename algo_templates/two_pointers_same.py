def two_pointers_same(arr):
  slow, fast = 0, 0

  while fast < len(arr):

    current = process(arr[slow], arr[fast])

    if condition(arr[slow], arr[fast]):
      slow += 1

    fast += 1

