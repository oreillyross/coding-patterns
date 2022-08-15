import math

def summing_squares(n, memo = {}):
  
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  min_sqr = float("inf")
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i
    num_sqr = 1 + summing_squares(n - square)
    min_sqr = min(min_sqr, num_sqr)
  memo[n] = min_sqr
  return min_sqr
