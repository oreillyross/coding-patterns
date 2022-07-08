def generate_sums(weights, sums, sum, n):
  if n == 0:
    # set operations have a add as oppose to list which is append
    sums.add(sum)
    return 
  generate_sums(weights, sums, sum, n - 1 )
  generate_sums(weights, sums, sum + weights[n - 1], n - 1)


def knapsack_weight_only(weights):
  sums = set()
  n = len(weights)
  generate_sums(weights, sums, 0, n)
  return list(sums)
  
