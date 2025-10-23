def sliding_longest_flexible(input):
  initialize window, ans
  for right in range(len(input)):
    append input[right] to window
    while invalid(window):
      remove input[left] from window
      left += 1
    ans = max(ans, window)
  return ans
