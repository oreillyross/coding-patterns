# The steps to solve this are described below.

#   The function signature of the problem statement is

#   def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

# First step is to define a variable that will hold your result, you can call this ans
# then call a inner function defined as dfs that takes two arguments, paramaters are called start_index and num.
# The start_index gets incremented by 1 each time you go down the levels of the graph, so the idea behind this is that 
# once you have checked all the numbers in the range 1-9 up to the count of n
# the num is the accumulated answer which once dfs ends (ie you reached a valid leaf you can append this to ans array)
# after the base case check you need the last valid number in the num passed in recursively. This clever python trick gets you the last number in the 
# number by using % 10 (mod 10)
# then perform a if check to see if the modded digit, ie the least significant number (the last one at the end) is a valid number, i.e 
# greater than 0 then dfs down this path, increase the start_idx, and append the valid digit to the end by multiply the original
# by 10 and then simply add the new valid digit to this number, because it is within the 1-9 range it will essentially replace 
# the 0 at the least significant digit space.
# Then do the same if check on the modded value to see if it is less than 9 and dfs down this option to get a 
# possible option that is also valid, and do the same start_idx + 1, getting closer and closer to base case
# make sure to also * 10 the num to make space and append the next valid digit.
# final thing is to call the dfs function starting at 1, and the range value i so a for loop 1 - 9.
# then return the ans







