# Trees 

- Is a data structure made up of nodes, each node can point to a number of nodes, not just one.
- Order of elements not important in a tree
- It is a non-linear data structure
- Nodes without children are called leaves

## Binary Tree
- Each node can have 0, 1 or 2 children. Left and right child

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


----

### Binary Search

- Searching for an element in a list, the list must be sorted
- Find the mid-point, if element return value, or bigger than then check right hand side, and divide, if smaller, check left side, and divide.

---

# Graphs

* Used to represent relationships with entities
* Vertex is the node, edge is the relationship
* The degree of a node is how many edges it connects to.
* A path is a way to get from one vertex to another vertex. Can be cyclic, or acyclic.
* An undirected graph with no cycles is actally just a tree.

<em>A forest is a disjoint of trees</em>

A graph is two Vertices (V) connected by an edge (E). A graph can be directed or undirected. Undirected represent two way relationships. Directed can show hierarchy.

---

### Adjacency matrix

This is a way to represent a graph. 

#### Use one of the three standard ways to represent graphs:

1. Adjacency Matrix
2. Adjaceny List
3. Adjacency Set

##### Adjacency matrix
This is a matrix with rows and columns. A matrix is just a table, The row labels and the columns labels represent the vertices.
Each cell represents the relationship between the vertices. i.e. the edges.
    <pre>
    a b c d e
a   0 1 0 0 0
b   1 0 1 1 0
c   etc. etc.

</pre>

This can be used to represent directed and undirected relationships.

##### Adjacency List
* Each vertex is a node
* Each vertex has a pointer to a linked list
* This linked list contains all the other nodes this vertex connects to directly

- Adjacency lists are more space-efficient than adjacency matrices
- Adjacency lists not best representation of graphs
- Order of vertices in adjacency list doesn't matter, same graph can have multiple representations
- Deletion becomes tricky, looking through all adjacency lists to remove the node from all lists
    - A way around this is to use an Adjacency set, sort of binary seach tree.
 
##### Topological sort
Take all the indegree from each node, remove the nodes with 0, then recalculate indegrees, and repeat to 
get a traversal. Only applies to directed and acyclic graphs.

| Description                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One of the best explanations I have found on Khan's algorithm, which is a classic topological sort algorithm, can be found [here](https://ilque.me/2024/07/02/kahns-algorithm-for-topological-sorting-a-comprehensive-guide/). |

---

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

