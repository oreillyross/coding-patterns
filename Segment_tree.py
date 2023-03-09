# Segment Tree

# has the following two textbook operations
# update(index, val)
# queryRange(L,R)

# both operations can be run in O(logn) time
# Uses divide and conquer strategy like in the merge sort alogrithm
# mid = L(arr) / 2, so left baranch is L, M and right branch is M + 1, R
# The terminating case is when array is length one, base case

class SegmentTree:
  def __init__(self, total, L, R):
    self.sum = total
    self.left = None
    self.right = None
    # Below are L and R indexes, not the actual nodes.
    self.L = L
    self.R = R
  
  # O(n)
  @staticmethod
  def build(nums, L, R):
    if L == R:
      return SegmentTree(nums[L], L, R)
    M = (L + R) // 2
    root = SegmentTree(0, L, R)
    root.left = SegmentTree.build(nums, L, M)
    root.right = SegmentTree.build(nums, M + 1, R)
    root.sum = root.left.sum + root.right.sum
    return root
   
