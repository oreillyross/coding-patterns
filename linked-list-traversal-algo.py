
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

def printList(head):
	current = head
	while current is not None:
		print(current.val)
		current = current.next

def printList2(head):
	if head is None:
		return None
	print(head.val)
	printList2(head.next)


# printList(a)
printList2(a)