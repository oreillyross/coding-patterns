class LinkedList:
	def __init__(self):
		self.head = None
    
    def __repr__(self):
        nodes = []
        curr = self.head
        
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + '->'.join(nodes) + ']'

    
    
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __repr__(self):
		return repr(self.val)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# classic imperative solution
def printList(head):
	current = head
	while current is not None:
		print(current.val)
		current = current.next

# recursive classic traversal
def printList2(head):
	#base case
	if head is None:
		return None
	# do something with each node
	print(head.val)
	#recursion
	printList2(head.next)

    
 def reverse(head):
    """Reverse the list in-place"""
    
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
        

# printList(a)
printList2(a)
