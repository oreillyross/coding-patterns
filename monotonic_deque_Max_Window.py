from typing import List
from collections import deque

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    # Instantiate an empty double-ended queue to store indices of the elements
    q = deque()
    # Initialize an empty list to store the maximum values of each sliding window
    res = []
    
    # Iterate through the nums array in O(n) time, processing each element one by one
    for i, curr in enumerate(nums):
        # Maintain the monotonic decreasing property of the deque:
        # Remove indices from the back of the deque while the current element (curr)
        # is greater than or equal to the element at the index stored in the deque.
        # This ensures that elements in the deque are in decreasing order, and 
        # the front of the deque always holds the maximum element for the current window.
        while q and nums[q[-1]] <= curr:
            q.pop()

        # Append the current index to the deque. The deque will now store valid indices
        # where the values maintain the monotonic decreasing property.
        q.append(i)
        
        # Check if the front of the deque (q[0]) is out of the current window:
        # The front of the deque may correspond to an index that is no longer valid
        # because it is outside the current window range. If the index at q[0] is
        # equal to i - k (i.e., just outside the left boundary of the window),
        # remove it by popping from the front (popleft).
        if q[0] == i - k:
            q.popleft()

        # Once the window has reached size k (i >= k - 1), append the current maximum
        # to the result list. The maximum value for the current window is the element
        # at the index stored at the front of the deque (q[0]), as the deque is 
        # structured to keep the largest element at the front.
        if i >= k - 1:
            res.append(nums[q[0]])

    return res
