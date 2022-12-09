# Selection sort
# every iteration -> one element compared with every other to find smallest -> place in first positions, then in second position, repeat
# rearrange in-place to save on space
# O(n^2)
# not a stable sort, equal elements might be re-arranged


# compare 15 with all other elements, pcick the smallest one
# place at front of array, swop the 15 with 11
# shift search area plus one, so start at 32 -> to end 

nums = [15,32,26,11,36,19,42,44,14]
testsortednums = [11,14,15,19,26,32,36,42,44]

def selectionsort(nums):
  for i in range(len(nums) - 1):
    minIdx = i
    for j in range(i + 1,len(nums)):
      if nums[j] < nums[minIdx]:
        minIdx = j
    nums[i], nums[minIdx] = nums[minIdx], nums[i]
  return nums
  
  

assert(selectionsort(nums) == testsortednums)
  
# Bubble sort
#===================================================
nums = [15,32,26,11,36,19,42,44,14]

# Iterate through list
# compare first two elements, which is larger, move it to the right
# move one, compare next two elements, move or swop positions to get biggest element to the right
# Keep bubbling up the biggest element.
# once biggest element to the right, repeat, the process, untill all elements are sorted
# O(n^2) but its a stable sort, same values will not be swapped., O(1) space

nums = [15,32,26,11,36,19,42,44,14]
testsortednums = [11,14,15,19,26,32,36,42,44]

def bubblesort(nums):

  for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
  return nums    
    
print(bubblesort(nums))
assert(bubblesort(nums) == testsortednums)

# Insertion sort

# Has two parts, sorted list to the left, and an unsorted list to the right
# compare two numbers adjacent to each other, move smaller number to the left, keep iterating
# sublist is sorted and grows to be equal to the entire list
# assume sorted list is size of 1, and grows to be size of original list
# O(n^2) stable sort, same values remain in the same spot, no swops happen
# Nearly sorted lists complete very quickly like in bubble sort, adaptive sorting algorithm

nums = [15,32,26,11,36,19,42,44,14]
testsortednums = [11,14,15,19,26,32,36,42,44]

def insertionsort(nums):
  # after each inner loop, the sorted left side gets ignored in this outer loop as it iterates over the list naturally
  for i in range(1, len(nums)):
    # similar to bubble sort, but trickle smallest number down to the left
    for j in range(i - 1, -1, -1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j +1], nums[j]
  return nums


print(insertionsort(nums))
assert(insertionsort(nums) == testsortednums)


# Shell sort
# Shell sort uses insertion sort and the entire list is divided and those sublists are sorted
# exact complexity depends on increment values chosen
# somewhere between O(n) and O(n^2)

# Merge Sort

# This is a divide and conquer algorithm, create smaller sub-problems
# list broken down into smaller and smaller lists recursively
# list should finally contain only one element, this is the one element which is sorted
# Then move into conquer phase, so merge sublists into each other to get a single sorted list
# Divide and conquer with recursion, solve trivial case, then build up as recursion unwinds
# O(nlogn) time O(n) space, stable algorithm, but not adaptive
# The algo is only stable if we handle the equality case in the merge step of the algorithm left <= right
# Two branch recursion, divide problem by two until base case is one item, then solve sub problmes, compare two items at a time


def merge(left, right):
    # declare sorted array to populate
    sorted = []
    l = r = 0
    # while either list still has indexable elements
    while (l < len(left) and (r < len(right))):
        # check which is smaller and append it to sorted list, increment wither l or r pointer
        if left[l] <= right[r]:
            sorted.append(left[l])
            l +=1
        else:
            sorted.append(right[r])
            r += 1
    
    #use built-in extend method to tack on which ever list is left
    sorted.extend(left[l:]) 
    sorted.extend(right[r:]) 
    
    return sorted

def sortArray(nums: List[int]) -> List[int]:
        # base case if one element in list, list is sorted
        if len(nums) <= 1:
            return nums
        # divide step, find mid point
        mid = len(nums) // 2
        # get left and right side, with list indexing
        left = sortArray(nums[:mid])
        right = sortArray(nums[mid:])
        # call and return the merge step on each recursive split list, so going up 
        return merge(left, right)


# Quick Sort
# ===================================================================================
# Often the native sort functions is the quick sort
# divide and conquer approach, unlike merge sort, the index is based rather on a pivot.
# The pivot is one element from the list
# All elements smaller, go on one side, all larger go on the opposite side of the pivot
# The sub lists all have their own pivots
# no exact science, can pick first, last, or middle of list.
# recursively apply this divide, slect pivot, and apply finding the rightful place for each pivot element
# Needs a partition function, to find the pivot, and move elements before or after pivot
# Also needs a quicksort function which makes the recursive calls to the sub-lists and calls the partition function above
# O(nlogn) with base of logarithm of 2, divide, sapce is O(logn) and worst case O(n)
# unstable sort, and not adaptive

TODO IMPLEMENT THE QUICK SORT ALGO









