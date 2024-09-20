The steps to solve this are described below.

  The function signature of the problem statement is

  def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

First step is to define a variable that will hold your result, you can call this ans
then call a inner function defined as dfs that takes two arguments, paramaters are called start_index and num.
The start_index gets incremented by 1 each time you go down the levels of the graph, so the idea behind this is that 
once you have checked all the numbers in the range 1-9 up to the count of n
the num is the accumulated answer which once dfs ends (ie you reached a valid leaf you can append this to ans array)
after the base case check you need the last valid number in the num passed in recursively. This clever python trick gets you the last number in the 
number by using % 10 (mod 10)

