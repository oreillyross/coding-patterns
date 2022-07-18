from heapq import heappop, heappush
from typing import List

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # create an empty result list
    res = []
    # start of the heap data structure, empty array
    heap = []
    # iterate over the lists, and store a tuple of three values in heap
    # the first value of the tuple is the key used to determine min heap value
    for curr_list in lists:
        heappush(heap, (curr_list[0], curr_list, 0))
    # whil there are still items on the heap take the next min value
    while heap:
        # pop the tuple of three values, the second item and third item are passed to make sure the list is iterated if a value is taken
        val, curr_list, index = heappop(heap)
        res.append(val)
        index += 1
        # this is the iteration logic to get to termination point of reaching the end of a list.
        if index < len(curr_list):
            heappush(heap, (curr_list[index], curr_list, index))
        
    return res
