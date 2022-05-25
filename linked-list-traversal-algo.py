
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

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


# printList(a)
printList2(a)