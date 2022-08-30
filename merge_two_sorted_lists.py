#iterative solution to problem

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current_1 = list1
        current_2 = list2
        
        dummy_head = ListNode(None)
        tail = dummy_head
        
        while current_1 is not None and current_2 is not None:
            if current_1.val < current_2.val:
                tail.next = current_1
                current_1 = current_1.next
            else:
                tail.next = current_2
                current_2 = current_2.next
            tail = tail.next

        if current_1 is not None:
            tail.next = current_1
        
        if current_2 is not None:
            tail.next = current_2
            
        return dummy_head.next
        
