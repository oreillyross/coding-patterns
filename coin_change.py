# Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins 
# required to create the amount. You may use each coin as many times as necessary.
# If it is not possible to create the amount, then return -1.

# #1 start with brute force solution, and core recursive pattern
# #2 memoise the solution
# #3 deal with edge cases, failing tests

def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  #3 deal with edge case where no soluton is found, need to return -1 not inf.
  if ans == float("inf"):
    return -1
  else:
    return ans

#2 break out main function into a helper, and pass extra argument memo for hash memo solution
def _min_change(amount, coins, memo):
  
  #2 short circuit, if we have this value already calculated
  if amount in memo:
    return memo[amount]
  
  if amount < 0:
    return float("inf")
  
  #1 base case, if you have zero amount, you need 0 coins to get that amount
  if amount == 0:
    return 0
    
  #1 need some min value logic, in python its below. in javascript use Math.Infinity
  minWays = float("inf")
  
  #1 iterate through all the coins available, and recursively call min_change, making amount smaller and smaller
  #1 recursive leap of faith is to add one for each call as you are taking a coin each time
  for coin in coins:
    numWays = 1 + _min_change(amount - coin, coins, memo)
    
    #1 min value logic to store minimum most value
    if numWays < minWays:
      minWays = numWays
  #2 store the calculated value always where you return the stored value.
  memo[amount] = minWays
  #1 return the number of coins used to get min ways
  return minWays
