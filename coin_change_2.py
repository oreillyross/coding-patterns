def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  
  # memoise function calls
  key = (amount, i)
  
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  total_ways = 0
  
  # prevent list out of bounds error
  if i == len(coins):
    return 0
  
  coin = coins[i]
  # In python the range function second argument is exclusive, so add 1
  # to get to correct end range
  # floor using // so we have at most coins, and then a remainder
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, i + 1, memo)
  
  memo[key] = total_ways
  return total_ways
