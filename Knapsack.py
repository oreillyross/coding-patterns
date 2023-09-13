# Notes on unbounded knapsack and grokking this algorithm
# This pattern is very similar to the classic 0/1 Knapsack pattern
# Common interview questions are the backpack or knapsack problem
# 


def generate_sums(weights, sums, sum, n, memo):
  if memo[n][sum]:
    return
  if n == 0:
    # set operations have a add as oppose to list which is append
    sums.add(sum)
    return 
  generate_sums(weights, sums, sum, n - 1 )
  generate_sums(weights, sums, sum + weights[n - 1], n - 1)


def knapsack_weight_only(weights):
  sums = set()
  n = len(weights)
  total_sum = 0
  for weight in weights:
    sum += weight
    memo = [[False for x in range(total_sum + 1,)] for y in range(n + 1)]
  generate_sums(weights, sums, 0, n, memo)
  ans = []
  for sum in sums:
    ans.append(sum)
  return ans
  
