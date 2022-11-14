# Trees 

- Is a data structure made up of nodes, each node can point to a number of nodes, not just one.
- Order of elements not important in a tree
- It is a non-linear data structure
## Binary Tree
- Each node can have 0, 1 or 2 children

## Balanced tree
 - A highly skewed tree can be a list, the complexity will be O(n)
 - A balanced tree, will have worst case complexity of O(logn)
 
### Binary Search tree
- Ordered binary tree but with extra characteristics
  -  Left subtree less than or equal to value of the node
  -  Right subtree greater than the value of the node
  -  Recursively every node obeys this constraint
 ####  Insertion
 - exactly one place can be added
 - Its placement will always be as a leaf node, where its parent either has no, or one child.
 #### Lookup
 - exactly one place where it can be found
- Keep iterating left or right subtree
- either find the value, successs, or find a null value, then its a failure

#### Min or max value in a BST
 - Min value can be found by traversing recursively the left subtrees until you hit a leaf node.
 - Max value can be found along right subtrees

#### Common operations in a Binary Search tree
  * Max depth of a Binary tree
  * Sum paths in a BST
- 


### Binary Search

- Searching for an element in a list, the list must be sorted
- Find the mid-point, if element return value, or bigger than then check right hand side, and divide, if smaller, check left side, and divide.

# Graphs



# Traversal of Trees and Graphs

#### Breadth First Traversal
  * vist all nodes at every level before moving on to the next level
  * level 0 is the root node, first node to visit
  * Use a queue data structure under the hood
  * add node, dequeue, then add its left and right children to the queue, repeat as long as queue is not empty (FIFO)

#### Depth First Traversal

- Pre-order (node, then each of its children)
- In-order (left first, then the node, then right)
- Post-order (both children first then node itself)

  * Go stright to leaf node, then go to next node.
  * Pre-order, in-order, post-order
  * Use recurision and stack under the hood.
  * Base case is when root node is null or empty

