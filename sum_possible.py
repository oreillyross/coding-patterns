def sum_possible(amount, numbers, memo = {}):
  
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return False
  if amount == 0:
    return True
  
  for num in numbers:
    if sum_possible(amount - num, numbers):
      memo[amount] = True
      return True
  memo[amount] = False
  return False
