# Merge sort pseudocode
# start with 2 branch recursion breaking the list down in the middle, and at each 
# depth or level keep breaking it down
# base case is when you get to one element, the leaf node, this is one element
# and is already sorted.
# Then build up the list again and at each level
# do the merge
# so have three pointers jkl, j for left list, k for right list and l for 
# built up sorted array.
# iterate while left and right list both have elements
# compare which element is bigger, append that element and increment pointer
# at each while loop increment l pointer.

# at the end either of the lists could still have elements, (remember sublists are sorted)
# can append the one or other list to arr.

# The patterns applied in this code include:
# the two pointers pattern of code, iterating through two lists with two pointers
# the mergsort part, the breaking up of the list intow pices recursively is done in 
# log n time. essentially the opposite of 2^n for fibonacci sequence recursion
# The merge subroutine is done in O(n) time, as entire array essentially needs to be traversed.




def merge_sort(list):
  
