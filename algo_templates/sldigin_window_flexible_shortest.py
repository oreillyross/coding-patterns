def sliding_window_shortest(input):
  initialize window ans
  left = 0
  for right in range(len(input)):
    append input[right] to window
    while valid(input):
      ans = min(ans, window)
      remove input[left] from window
      left += 1
  return ans
