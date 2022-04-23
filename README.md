# coding-patterns to help as an aide-memoire



## Online tools to practice for technical interviews

* [Structy](https://structy.net/) This site offers a online playground along with course videos and explanations for practicing data structures and algorithms
* [TS Playground](https://www.typescriptlang.org/play?#code/Q) This is a good option for a technical interview if you have to code a solution to a problem using typescript.
* [Geeks for Geeks] (https://practice.geeksforgeeks.org/)
* [Interview Cake](https://www.interviewcake.com/)
* [Leet code](https://leetcode.com/)
* [Neet code](https://www.youtube.com/channel/UC_mYaQAE6-71rjSN6CeCA-g) A youtube channel from a a guy who is now a Google engineer who created videos in python of many Leet code challenges
* [Algo.monster] A site which distills essential algorithms, data structures and techniques for interviewing. Created by former Google engineers.

General Programming concepts:
Be able to define, describe and demonstrate through examples the following concepts:

1. Closure


2. Partially applied function
3. Currying
4. Higher Order Functions
5. Event loop
   

## General Patterns to start solving a problem

* Start with Brute Force, even if you know it is not efficient it will lead to other considerations to solve the problem
* Keep track of the best answer so far in one pass of the problem, see if you can break it down into pieces
* Consider early to use a hash map, even if you don't know how yet as it is used in solving many problems generally.
    - If your brute force solution results in a nested __for loop__ this should indicate you can almost certainly use a hashmap O(1) lookup to reduce the complexity from O(n^2) to O(n). Use the ```if (num in hash)``` check 



## Algorithms to know

### Two pointers
* A common strategy for keeping track in array and string based problems
* Two pointers can be used to track slices of a string, the below snippet highlights a use case

```javascript
            const uncompress = (s) => {
            
            let left = 0;
            let right = 0;
            const output = [];
            
            const isNumber = new RegExp(/\d/)
            
            for (let i = 0; i < s.length; i++) {
                if (isNumber.test(s[i])) {
                    right += 1;
                    continue;
                }
                const times = s.slice(left, right);
                output.push(s[i].repeat(times));
                left = right + 1;
                right = left;
            }
            
            
            
            return output.join('')
            };


            uncompress("2c3a1t");
```



### <p style="color: lightgreen">Sorting Algorithms</p>

#### Insertion sort
* This has an O(n^2) complexity because of the two for loops.
* Key to this is iterating over the unsorted array starting from the first element, and doing the sorting in-place.
* Then store the first element to compare inside the second for loop
* the second for loop starts at j -1, so the previous current element, and while j initialised to i - 1 is >= 0 and the current element is bigger than current
 move the element to the right;
 * finally after exiting this for loop replace element at j + 1 to the current value.
 * return the (now) sorted array

 ```javascript
            function sortList(unsortedList) {
                
            // insertion sort algorithm
                for (let i = 1; i < unsortedList.length; i++) {
                let current = unsortedList[i];
                let j;
                for (j = i - 1; j >= 0 && unsortedList[j] > current; j--) {
                    unsortedList[j + 1] = unsortedList[j];
                }
                unsortedList[j +1] = current;  
                }
                
                return unsortedList;
                
            }
 ```
 #### <p style="color: lightblue">Merge sort</p>
 * This algorithm uses a __`Divide and conquer`__ strategy
 * Because it needs to split the arrays to some base case (when only one element exists) recursion is a good implementation
 * alternatively it can be solved using the bottom-up approach
 * The complexity is O(n log n), which is efficient
 * The algorithm requires two functions, one which takes two sorted arrays and returns one sorted array, a second function which recursively divides arrays.
 * The below details the general algorithm in javascript

```javascript

            const unsortedArr = [31, 27, 28, 42, 13, 8, 11, 30, 17, 41, 15, 43, 1, 36, 9, 16, 20, 35, 48, 37, 7, 26, 34, 21, 22, 6, 29, 32, 49, 10, 12, 19, 24, 38, 5, 14, 44, 40, 3, 50, 46, 25, 18, 33, 47, 4, 45, 39, 23, 2];

            function merge<T>(s: T[] ) {
            // base case for recursive function. i.e. if it is one item in array, array is sorted.
            if (s.length <= 1) {
                return s;
            }
            // divide and conquer, split array in half
            const mid = Math.floor(s.length /2);
            const left = s.slice(0, mid);
            const right = s.slice(mid);
            // recursive case, keep calling merge function until sub-arrays are split over and over
            const left_sorted: any = merge(left);
            const right_sorted: any = merge(right);
            // perform the sorting step using the utility function which merges two sorted arrays. This returns many of the sub arrays sorted
            return _mergeSortedArrays(left_sorted, right_sorted);

            }

            function _mergeSortedArrays<T>(a: T[], b: T[]) {
                
                const sorted = [];
                // keep finding the smallest element between the two sorted arrays. The shift operation removes the first element, thus making array
                // smaller and adhering to while loop condition
                while (a.length && b.length) {
                sorted.push(a[0] <= b[0] ? a.shift() : b.shift() );
                };

                // this is a short-cut, using ES2106 syntax, it spreads the sorted array, and concatenates the remaining two arrays. Because
                // the condition above in the while loops guarantees only one array could still cnotain values, we can safely spread both arrays
                // which will either append all remaining from one of the arrays and append an empty array which has no effect.
                return [...sorted, ...a, ...b];
            };

            console.log(merge(unsortedArr))

```

### Binary Search 
 - The precondition to searching is that the __array must be sorted__.
 - Key pieces are two pointers, one initially pointing to the first value (low pointer), the other pointing to the end of the array (high pointer).
 - algorithmic step is to find the midpoint (floored for whole number), check if it matches the target value, or if its lower than target value, move low pointer 
 to the midpoint index, if its higher, move the high pointer to the mid point index, repeat until target found or low matches high index. Then no match.
 - This gives a complexity of __O(log n)__ runtime.
 
    - pseudo code steps    
```
       * while the two pointers dont cross
       * find midpoint index
       * check if target higher, move low pointer to midpoint + 1
       * if target lower move high pointer to mid - 1 
       * else it is equal to mid, return mid as its the index
  
       * all else fails return -1
```
```javascript
        function binarySearch(arr, target) {
    
            let left = 0;
            let right = arr.length - 1;
            while (left <= right) {
            const mid = left + Math.trunc((right - left) / 2);
            if (arr[mid] < target) {
                left = mid + 1;
            } else if (arr[mid] > target) {
                right = mid - 1;
            } else {
                return mid;
            }
            }
    
          return -1;
        
        }
```
* The binary search can also consist of a __find boundary__ element, which is essentially finding the 
next True element (or the first true element) in a true or false array.
* The condition or check at the midpoint element might indicate a true or false condition, whereby you
  update the boundary index and shift the left or right pointer accordingly. 
  * The below [Minimum in Rotated Sorted array](https://algo.monster/problems/min_in_rotated_sorted_array) is a good example.

```javascript
    function findMinRotated(arr) {
    let left = 0;
    let right = arr.length - 1;
    let boundary_index = -1;
    while (left <= right) {
        let mid = left + Math.trunc((right - left) / 2);
        // if <= last element, then belongs to lower half
        if (arr[mid] <= arr[arr.length - 1]) {
            boundary_index = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return boundary_index;
}
  
```

#### Serializing and deserializing an Array

``` 
  PSEUDO CODE:
    - to serialise: 
        - create a result array, 
        - recursively call a dfs function, passing the next node in, and a reference to the result array to be populated inside recursive call.
        - return array as joined " ";
        Normally in the recursive call you think about the return value, and what state, in this case we only worry about the state, which is array passed in as reference.
        - base case is leaf node, if (!node) push 'x' to array and return void.
        - push the node.val and then 
        - recursively call function passing the left and right nodes in calls respectively, along with state.
    - to deserialise:
        - Use the trick of creating an iterator from the string split as array, the arr[Symbol.iterator]() will do it 
        - pass this in as the only argument to dfs function for deserialising,
        - inside the function first get the next value by calling iterator.next(),
        - if it is an 'x' char then simply return void, as its a leaf node, // base case to get out of recursion
        - otherwise create a new Node, passing parseInt(value, 10)
        - then with that node call left and right recursive calls passing result back to curr.left or curr right.
        - then return the current node, which goes back into recursive call.
```

```javascript
    function serialize(root) {
        const res = [];
        dfs_serialize(root, res);
        return res.join(" ");
    }

    const dfs_serialize = (node, res) => {
    if (!node) {
        res.push("x");
        return;
    }
    res.push(node.val)
    dfs_serialize(node.left, res)  
    dfs_serialize(node.right, res)
    }

    function deserialize(s) {
        return dfs_deserialize(s.split(" ")[Symbol.iterator]())
    }

    const dfs_deserialize = (nodes) => {
        const {value} = nodes.next();
        if (value === "x") return;
        const newNode = new Node(parseInt(value, 10))
        newNode.left = dfs_deserialize(nodes)
        newNode.right = dfs_deserialize(nodes)
        return newNode;
    };
```

### Topological order
- Key to victory is to build a hash map of the parents and their connections, so numParents = {};
- Also have an array called ready, which takes the nodes that have a count of 0 in the numParents object
- Add the last node in ready to the order array, return this order array as the final result. 

## Data Structures

### Trees
- know the difference between inorder (left, root, right), preorder (root, left, right) and postorder (left, right, root) traversal, this applies to depth-first searches. 
  - __Post order traversal__
    - This is used to determine if a tree is balanced.
    -  

* Key to reasoning about tree like structures is to think from the perspective of a node. get inside recursive leap of faith logic.

```
  // TEMPLATE FOR DFS on TREE
    function dfs(node, state) {
        if node is null
          ...
          return
        left = dfs(node.left, state)  
        right = dfs(node.right, state)  
        ...
        return ...
    }

```

 __<span style="color: lightgreen">Two things</span>__ to decide on when thinking through recursion
 1. The return value (passing value up from child to parent)
 2. Identifying the state (passing value down from parent to child)

In essence when solving a problem with recursion either use the return value (partition and merge) or store a global variable that is updated based on each recursive call.

#### <p style="color:lightgreen">Combinatorial search on trees</p>

Think about the problem as using a binary tree as a framework to generate all possible subsets. Whilst you don't code the Binary tree nodes, you can use the same recursive DFS techniques to visit all the possible combinations.

- Generally the height of the tree = the number of input n's. The complexity can be generalised for n to be O(2^n) in time and space. 

- Three steps:
1. Identify the state(s)
2. Draw the state-space-tree
3. DFS/backtrack on the state space tree

  ### Backtracking
* This is common in problems which require a bruteforce approach.
* Think of the problem in terms of a decision tree which branches out exponentially, i.e. based on the number of inputs
* upon reaching the leaf nodes you can _backtrack_ up the tree to the root node to get each and every variation.
* problems solved with this approach include the [Letter Combinations](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) problem from Leetcode.

* use a recursive function inside your main function to build the result recursively.

##### Backtracking template
```javascript
    function dfs(node, state) {
        if __state__ is a solution {
            report(state) // add state to final result list
            return
        }

        for (child of children) {
            if child is a part of a potential solution
            state.add(child) // make move
            dfs(child, state)
            state.remove(child) // backtrack
        }
    }
```    

Some real javascript code to demonstrate:

```javascript
    function dfs(root, path, res) {
        if (root.children.every(c => !c)) {
        res.push(path.join("->"))
        return;
        }
        
        for (let child of root.children) {
        if (child) {
            path.push(child.val);
            dfs(child, path, res);
            path.pop();
        }
        }
    }
```

### Solving the permutation problem with pseudocode

1. Identify the states, so you need to know the full path, and when it has been reached to record this, pass it along, and second state is to know which letters have been used.
2. DRAW THE TREE (State-space-tree).
3. Apply DFS and backtrack template.
    - base case is when path.length == letters.length
    - then append the path to res (found one path), and return
    - then __for__ over the letters and check if used, continue, otherwise path.push the letter, mark it as used and recursively call the dfs function.
    - then backtrack, pop letter from path and mark letter[i] as false 
    - finally call the function first time, passing [] for path, Array(letters.length).fill(false)
    and return res

```javascript
    function permutations(letters) {
        const res = [];
        dfs([], Array(letters.length).fill(false), res)
        return res;
        
        function dfs(path, used, res){
            if (path.length === letters.length) {
            res.push(path.join(""));
            return;
        }  
        for(let i = 0; i < letters.length; i++) {
          if (used[i]) continue;
          path.push(letters[i]);
          used[i] = true;
          dfs(path, used, res);
          path.pop();
          used[i] = false;
        }
        return res;
    }
  }
```
#### [Generate parenthesis](https://leetcode.com/problems/generate-parentheses/)

This is a classic combinatorial problem which requirss searching all combinations and backtracking using dfs.
- Think about your base aase to populate one valid path. This is where drawing the state-space tree will help. 
- In this case it is when the accumulated path is equal to the 2 braces (2) * n;
- Update result, and return
- then the two recursive cases are either validly inserting a open brace or inserting a valid close brace.
- Then recursively call function, updating state, which is count of open or closed brace
- and backtrack, after recursive call, so pop()

__see below code__ 

```javascript
    var generateParenthesis = function(n) {
        
        let result = [];
        const gen = (braces = [], open = 0, closed = 0) => {
            
        if (braces.length === 2 * n) {
            result.push(braces.join(""));
            return;
        } 
            
        if (open < n && open >= closed) {
            braces.push("(");
            gen(braces, open + 1, closed);
            braces.pop();
        }
            
        if (closed < n & open >= closed) {
            braces.push(")");
            gen(braces, open, closed + 1);
            braces.pop();
        } 
        }
        gen();
        return result;
    };
```

### [Word Break (Combinatorial problem using memoization)](https://algo.monster/problems/word_break)

- This problem calls for using one state variable i, and then the state-space-tree is the words array choices one can make
- There will be some overlapping subproblems which can be memoized

```javascript
        function wordBreak(s, words) {
            // used to store the previous solutions found in teh decision state-space-tree
            const memo = {};
            // kick off the function call, returning the result wither true or false, pass in previous args, as well as 0, to track the recursive end condition
            return dfs(s, words, 0, memo)
            
        }

        const dfs = (s, words, i, memo) => {
        // base case is if the length of the string is equal to the index i, then all options can fit in the original string
        if (i === s.length) return true;
        // short-circuit call if already seen this solution in the state-space-tree
        if (i in memo) return memo[i];  
            
        // track the found state
        let found = false;
        // classic dfs search algorithm, for...of with recursive call based on condition
        for (let word of words) {
            // start at the ith index and slice until the end of string, i.e whatever still needs to be checked
            // check if the string starts with the word, each word in list will be checked
            // if it does then recursively call the dfs function to check the rest of the string, and increase i to just after the previously found word in string
            if (s.slice(i).startsWith(word)) {
            if (dfs(s, words, i + word.length, memo)) {
                found = true;
                break;  
            };
            }
        }  
        memo[i] = found;
        return found;  
        }
```

#### Balanced binary tree
* Determine if a tree is balanced. The definition of a balanced tree is the following:
  * The left and right subtrees of every node should differ by no more than 1 in height. 
  * Use the post-order traversal (left, right, root)

#### Binary tree
- Needs to meet three conditions:
    - Have only one root,
    - have a unique path between root to leaf node
    - each node can have 0, 1 or at most two children.

    __Remember an Empty tree is also a valid binary tree__


### [DFS Return all node values](https://structy.net/problems/depth-first-values)

   - There are two ways to approach this problem.
    - It forms the basis of DFS algorithm.
    
    * __iterative__
        - Either iteratively, use a stack to push the root node
        - Then while stack.length then push value onto values array
        - recursively call dfs for left and right nodes if they exist
        - finally return values array.
    * __recursive__ 
        - think about your return values. in this case its an array
        - base case is empty node, return empty array.
        - return the value, then spread out the collection of dfs calls on left and then right.

```javascript
    const depthFirstValues = (root) => {
      return dfcount(root)
    };

    const dfcount = (node) => {
      if (!node) return [];
      return [node.val, ...dfcount(node.left), ...dfcount(node.right)]
    }
```

### [Lefty nodes problem](https://structy.net/problems/premium/lefty-nodes)
- Start with a helper function that takes a node, and a count of what level you are on
- put the helper function inside the main function to make use of the closure behaviour of javascript to get access to the returned values array.
- inside the helper function recursively call itself passing in the left and then the right nodes, and level + 1.
- the base case is if node is null and you push a value if values.length === level.

## Binary Search trees
 - A type of binary tree with these properties
  - An empty tree is a valid BST
  - Non-empty tree left < root > right
  - left and right subtrees are all BST themselves

### Valid Binary Search Tree

```
    Pseudo Code
    1. think about return values, i.e. all same type of boolean being bubble up through tree. true && false
    2. Think about state that needs to be mainteind through each recursive call, the min and max value range for a node to be BST true
    3. Try not to nest your resucrsive function in main function to avoid namespace collisions and call stack errors.
```

``` javascript
        function dfs(node, min, max) {
            
                if (!node) return true;

                if (!(min <= node.val && node.val <= max)) return false;
                return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
            }

        function validBst(root) {
            return dfs(root, -Infinity, Infinity) 
        }
```
### <p style="color: lightgreen">Invert BST</p>
- Think about return value, which is inverted subtree, swopping left with right
- Use the class Node constructor to return a new Node and pass in the root.val, then swop the left and right node in constructor function and recursively call function on each left and right nodes now swopped.
- also check upfront for !node and simply return void.

```javascript
    function invertBinaryTree(node) {
        if (!node) return;
        return new Node(node.val, invertBinaryTree(node.right), invertBinaryTree(node.left));
    }
```

### <p style="color: lightgreen">kth smallest number</p>
  - This can be solved using a inorder traversal, given the properties of a BST, the left most node is the smallest
  - Keep a global count, which is incremented each time a left node is visited.
  - when count === k you have found the kth smallest node, return its value.

```javascript
        function kthSmallest(bst, k) {
        let count = 0;

        const dfs = (node, k) => {
            if (!node) return null;
            let left = dfs(node.left, k);
            if (left) return left;
            count++;
            if (count === k) return node.val;
            return dfs(node.right, k);  
        }
        return dfs(bst, k);  
        }
```

### [Breadth first search, return level order elements in a multidimensional array](https://algo.monster/problems/binary_tree_level_order_traversal)
- Key to vistory is apply the usual BFS template, which is using a queue, then shift on the queue (underlying array)
- while queue has a length keep iterating. First for over the n count of current queue and push into a new level array,
- then for of the children, and push them into queue
- finally after push new level into result array,
- finally exit while loop and return multidimensional array

```javascript
        function levelOrderTraversal(root) {
            
            const queue = [root];
            const result = [];
            while (queue.length) {
                const level = [];
                const n = queue.length
                for (let i = 0; i < n; i++) {
                const node = queue.shift();
                level.push(node.val);
                for(let child of [node.left, node.right]) {
                    if (child) queue.push(child);
                }
                }
            result.push(level);  
            }
            return result;
        }
```
### Zizag level order traversal(https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
This is the same as above with some slight changes (adding a boolean flag)

## Heap
A heap data structure is a type of binary tree, which is mostly complete. Being mostly complete (i.e. leaf nodes are on the far left) allows for O(log n) lookup, and O(log n) insert and delete. 
A min and max heap, means the heap is mostly sorted, all levels are sorted, but not necessarily the values oneach level. This allows one to quickly start at the top (min heap will be smallest to largest going down) and find the node you are looking for, the real power over a normal a sorted array is that the insert and delete

# Graphs
* A depth first search of a graph uses a stack data structure behind the scenes
* A breadth first search of a graph uses a queue data structure behind the scenes

* Use <code>for ... in</code> to get access to all keys if given a object with __adjacency list__ to represent graph. For iterative inspection of each node.

```javascript
  // Usually take in an adjacency list as input.
  {
      a: [b,c],
      b: [d],
      c: [b, e],
      e: []
  }
// but it can also take and edge list, which needs to be converted to an adjacency list first
// A list where the index represents the node and the value at that index is a list of the node's neighbors:
  const graph = [[0, 1], [1, 2], [1, 3], [2, 3]];

```

### <em>edge list to adjacency list</em>
- create helper function buildGraph, pass in edge list (array of sub arrays)
- create empty graph object, return it at the end
- iterate (<code>for ... of</code>) through every sub array
- destructure the pairs of each sub array
- add each destructured item to the graph object if not in the graph, initialise it as an empty adjacency array.
* undirected graph -> push both items into each other's arrays.
* directed graph -> push only the second item into first array.

The terminology differs slightly with trees. When talking about graphs we say vist each __neighbor__, as technically they are not __children__ like in trees which have a acyclic top down structure.

* Use <code>for ... of</code> to get the values of an object, so in this case it would be the adjacency list itself




## Cyle detection algorithm
- use the white-grey-black pattern (have a visting, visited Set()

### Generic cycle detection algo

```javascript
   const shortestPath = (edges, nodeA, nodeB) => {
     const graph = buildGraph(edges)
     // 1. ADD VISITED SET INITIALISED WITH FIRST NODE IN BRACKETS
     const visited = new Set([nodeA])
     // 2. PASS IT ALONG IN ALL BFT CALLS
     bft(graph, nodeA, visited)
   };

   const bft = (graph, node, visited) => {

     const queue = [node];
     while(queue.length) {
       const node = queue.shift();
       for(let neighbor of graph[node]) {
         // 3. DO THE CHECK ONLY AT THE TIME YOU WOULD ADD IT TO THE QUEUE
         if (!visited.has(neighbor)) {
           queue.push(neighbor)
           // 4. ADD IT TO THE VISITED SET AS WELL AFTER ADDING TO QUEUE
           visited.add(neighbor)
         }
       }
     }
   }


   const buildGraph = (edges) => {
     const graph = {};

     for(let pair of edges) {
       const [a,b] = pair;
       if (!graph[a]) graph[a] = [];
       if (!graph[b]) graph[b] = [];
       graph[a].push(b)
       graph[b].push(a)
     }
     return graph;
   }

   const edges = [
     ['w', 'x'],
     ['x', 'y'],
     ['z', 'y'],
     ['z', 'v'],
     ['w', 'v']
   ];

   shortestPath(edges, 'w', 'z'); // -> 2
```

## <p style="color: lightgreen">Depth first traversal</p>
- this can be done iteratively or recursively
- it uses a stack as the underlying data structure
- remember the adjacency list. Start with the node you have, passed in to function
- Iterative - stack.length > 0, pop from stack, for of into adjacency list, push onto stack
- Recursive - use node value, for of into G[node] adjacency list, recursively call function
- be careful of directed versus undirected graphs, undirected graphs need a way to stop cyclic calls, so add a visited feature.

## <p style="color: lightgreen">Breadth first traversal</p>
* This can only be done iteratively using a queue, along with its shift() and push methods
* The below code demonstrates a use case, finding the shortest path, as it traverses level by level.

```javascript
      
      const graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
      }
 
     function shortestPath(graph, r, c) {
        
            const queue = [[r, 0]];
            const visited = new Set([r]);
            while (queue.length) {
              const [node, distance] = queue.shift();
              if (node === c) return distance;
              for(let neighbor of graph[node]) {
                  if (!visited.has(neighbor)) {
                    visited.add(neighbor)
                    queue.push([neighbor, distance + 1]);  
                  }
               }
            }
      }
    
    shortestPath(graph, 0,3))
```

## <p style="color: lightgreen">Island hopping logic</p>
  - You will need a graph in the form of an object where the keys are nodes and the values are adjacency lists.
  - You get access to the adjacency lists and are inclusive of all islands by using the <code>for ... in call</code> on the graph.
## <p style="color: lightgreen">Grid Graph problems</p>
Sometimes you will be presented with a grid graph, such as 
    ```
    [
        [W,W,L,W],
        [L,W,L,W],
        [W,W,L,W],
        [L,L,L,W],
        [L,W,L,W],
        
    ]
    ```

    This pattern apperas for problems such as __flood fill__ or __connected islands__ problem.
    - Use a nested for loop to iterate over every row and column and then apply a recursive pattern of exploring every neighbor, using a combination of visited logic and the delta pattern (up, down, left, right).

```javascript
        /* 
        #1 Iterative code as part of main algorithm
        #2 Cycle detection logic
        #3 Recursive logic to visit all neighbours
        
        */
        const islandCount = (grid) => {
        let count = 0;
        //#2 declare an empty set to store string representation of r + c locations
        const visited = new Set();
        
        //#1 iterate with nested for loops
        for(let r = 0; r < grid.length; r++) {
            for(let c = 0; c < grid[0].length; c++) {
            //#3 call it first time to kick things off
            // returns true or false, if true it means we have an island
            if (explore(grid, r, c, visited)) count += 1;
            }
        }
        return count;
        };


        const explore = (grid, r, c, visited) => {
        //#1 check if we are going outside of the grid graph at any point
        const rowInBounds = 0 <= r && r < grid.length;
        const colInbounds = 0 <= c && c < grid[0].length;
        if (!rowInBounds || !colInbounds) return false;
        
        //#3 first base case, if we have got to a dead end
        if (grid[r][c] === 'W') return false;
        
        const pos = `${r},${c}`
        if (visited.has(pos)) return false;
        visited.add(pos);
        
        //#3 recursively call the function on all the neighbors going up down, left and right
        explore(grid, r + 1, c, visited)
        explore(grid, r - 1, c, visited)
        explore(grid, r, c + 1, visited)
        explore(grid, r, c - 1, visited)
        
        //#1 if the call gets to this point then we can return true as we have succesfully traversed 
        // a L land island.
        return true;
        }


        const grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
        ];

        islandCount(grid); // -> 3
```
## <p style="color: lightgreen">Bipartite graphs and graph coloring</p>

<hr/>

# <p style="color: hotpink">Dynamic Programming patterns</p>

## brute force

- start with the classic reduction of the input in your recursive calls.
- where there is an array that needs to get smaller, rather pass in an extra argument, like i that keeps track of the position of the single element you are on.
- Think of this problem in terms of a binary tree, that has two branches, the input with the element, and the input with out the element.

### Duplicate value avoidance pattern
 - Add a parameter to recursive function call, default to null.
 - Carry out a check (if statement) before the recursive call to check.previous value with current value not the same.
 - update it with the current value in the recursive calling of the function

<hr/>

### Calculating complexity
- Terms that can be used to describe complexity include: 
    * Maximal efficient solution
    * linear complexity O(n)
    * Multi-linear comlpexity O(n+m), this would be the case where two __for loops__ follow each other.

## <div style="color: lightgreen; text-decoration: underline">Coding problems and their solutions (mostly taken from Leet code)</div>

### 0 1 1 2 3 5 8 problem 🗃️

- The key to this is to remember that you need to start with two numbers you already know. Otherwise you have nothing to add. 
- The recursive solution is WAAAY to ineficient, and a simple 0(n) for loop where you store the result in an array thus building up the Fibbonaci sequence.
- If you do use a recursive solution, definitely make sure you use memoization strategy, 
- If you want to look clever (or dumb) pull out Benet's formula to calculate the Fibonacci sequence.

### Two sums problem 
 - The brute force approach suggests two for loops giving 0(n2)
 - the introduction of a hash or map allows one to capture the value as the key in the kv store which later can be checked if the complement (i.e. the difference) between target value and the value being iterated.
 - This can be done in one pass, if the checks for equality are done before the hash map is further constructed. 

### Reverse words in a string
- Without using any of the ES5+ javascript functions such as split, filter, reverse and join one can create two for loops (2n) and construct the reversed words
- space requirements include two arrays
- an improvement would include starting at the back of the string and repeating same first for loop to end up with words reversed on the first iteration

### Add two numbers
- This problem expects you to know singly linked lists. 
- Store a reference to the current (dummy) linked list so you can get to it after the while loop terminates 
- It has a numbe of edgecases which can make it tricky. Remember the two input linked lists can be different lengths
- The trickiest edge case is remembering at the end there might be a digit to carry over which needs to be added to Linked List which is returned.

### Longest Palindromic substring
1. This problem can be solved using dynamic programming
2. In an interview setting the easier option is to use the expand from middle technique and loop over the string (0(n^2) is best case
3. The brute force solution is easiest to solve it but very poor performance n^3
4. Be careful of the classic index +1 problem

### Roman to Integer challenge ✔️
 - This problem can be solved in a **single for loop**.
 - **create a hash** of the roman numerals to numbers first
 - Then play on the fact that you know that if a Roman Numeral of higher value comes before one of lower value that it must be that value otherwise its a combination number and you can then subtract the higher value from the smaller value to get the correct number, i.e. V - I = 4, X - I = 9 and so on.

### isPalindrome ✔️
- Convert the number inputted to a string with toString()
- have a start index and end index and loop until start half way through string, if at any time the values being compared do not match then return false
- increment and finally return true once while loop exits.

### Matching Parens
- The classic solution involves adding the opening brace to a stack (using a array is fine with push)
- If a closing brace is found you need to use a hash to get original opening brace and see if it matches the stack.pop value
- if not return false, otherwise return true if the stack is empty at end of iteration of string
- A useful peek method to seee what is at the top of the stack, i.e. last item in the array. is the array method array.at(-1) === array[array.length - 1]

### [Coin Change](https://leetcode.com/problems/coin-change/)
- The recursive solution, needs a memoization strategy
- Keep a count of current coin, so track an i index
- This challenge expects one to use dynamic programming. Although it can be solved with recursion, the more performant solution uses the bottom-up approach.
- Key to this is ensuring when you run through all combinations of coins for each amount that you only store the minimum amount on each iteration. So Math.Min must feature.
- Similarly to initialise the array you need to use Number.Max_Value as oppose to 0 for the coin change number of variations problem. (these are similar but different)

 ### [Remove duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 🚩 ✔️
 - This problems expects you to do an in-place sort with no extra array in memory, so 0(1).
 - The time is 0(n) as you have to loop through and update right pointer until the value and previous value are not duplicates.
 - If new value found you can replace the value at left pointer index with new value, then increment left pointer.
 - You end up just having to return the left pointer which is the index + 1 after for loop gives number of unique entries. 

### [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) 🚴‍♂️
- brute force approach is to concatenate the arrays, sort them and then divide by two,
- Either return the sum of the median two values divided by two if its an even length merged array or return single odd middle value.
- The array must be sorted to ensure you can simlpy look up middle value.

### [Sum of left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) ♻️ ✔️
- Many problems dealing with binary trees will involve a recursive solution
- always remember the base case to ensure it exits
- Remember the key is its only left leaves, so not all left nodes.

### [Remove linked list elements](https://leetcode.com/problems/remove-linked-list-elements/) ♻️ ✔️ 🔗
- This can be solved recursively or iteratively
- recursive base case is null
- otherwise return either the head.next value to remove the current node if it is equal to the value to remove

### [Binary Tree Inorder traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) 
- remember the rules, inorder is left tree first, then root, then right tree.
- recursion is simplest, create a helper function to traverse.
- This can also be solved iteratively using a stack.

### [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- This can be done without converting number to a string
- Think about the base 10 fact of numbers, if you take the full number and % 10 it and then take that number * 10 you have the tail of the number
- keep adding this to the result - so num + result
- iterate through number with the number / 10 | 0 to make number smaller until it reaches 0 then exits loop
- Math.pow is your friend to check 2^31 bounds

### [Container with most water](https://leetcode.com/problems/container-with-most-water/) 🚩
- This is a classic two pointers problem, one at start and one at end
- keep a maxArea value, update as you move either the left or right pointer based on which value is lower.

### [Merge two lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- Classic linked list problem
- key to this is create a dummyNode upfront, then a seperate reference to the tail which gets updated.
- The dummy head can return the next right at the end which is the new correct head with merged lists
- then loop while both not null and check which is smaller, update the link with smaller node's val and increment that pointer,
- watch out for the catch where you need to also update the tail to the next node, so a tail = tail.next call at end (inside) of while loop

### [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)
- Think of this problem in ters of a 2D array, to give you the visual grid you need.
- Key to this is tracking if you are going down or going up in the rows. This will give you the zig zag pattern.
- Cover your edge cases first, either s is only one char, or length of s is shorter than number of rows given
- Then populate your empty 2D array based on the number of rows given
- Begin iterating through the string and push the char into each row inside the grid.
- check if your rowCount is at the end of numRows - 1 or if rowCount is at 0 then you need to reverse direction.
- Once all rows have been populated you can for...of the rows and join each to a returned result string.

### [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- dynamic programming problem, solved wither top-down, recursive with memoization
- or solved bottom up
- the following algorithmic steps describe a top-down approach:
 - create two pointers, i and j. recursively call function starting at 0 index for both
 - base cases include i and j being out of bounds (i.e. at end of length of both strings) return true
 - if j out of bounds, i.e. no more pattens to match return false
 - if i in bounds and s[i] matches p[j], or its a '.' sign store this in a match var // either true or false
 - Edge Case: if the next char is a '*' recursively call function with one of two decsions either advance j + 2, or i + 1
 - The above call either repeats the char or it does not
 - If there is a match (i.e match is true) then simply recursively call function incrementing each index (i +1, and j + 1)
 - If the recursive function is inside the main function, make sure to kick it off with a function call passing (0,0)
 
 ### [Two Sum II Sorted array](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
 - The solution recognizes the fact array is sorted and that a solution will always exist. 
 - Uses two pointers approach
 - while loop for left < right
 - one pointer starts at index 0, the other pointer starts at end of array
 - the algorithm either increases left pointer if sum of two values at each pointer is less than target
 - or it decreases right pointer if sum is greater than target
 - or returns tuple of indexes if a match is found

 ### [Three Sum problem](https://leetcode.com/problems/3sum/)
 * This is a combination of the Two sum problem.
 * The first step is to sort the incoming list, be explicit about the sorting function otherwise it won't sort properly on integers
    ```javascript
      nums.sort( (a, b) => a - b)
    ```
 * Once sorted loop over nums and within your loop carry out the Two sum logic, with __2 pointers__

 ### [Letter Combinations problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
 * Uses backtracking pattern
 * recursively build the tree
 * the base case is when your current string length is equal to the length of input, i.e all letters used
 * recursively build letters for each character iterated over.
 * O(n*4^n) not ideal.
 ```javascript
        var letterCombinations = function(digits) {
          
          const hash = {
              2: ["a","b", "c"],
              3: ["d","e", "f"],
              4: ["g","h", "i"],
              5: ["j","k", "l"],
              6: ["m","n", "o"],
              7: ["p","q", "r", "s"],
              8: ["t","u", "v"],
              9: ["w","x", "y", "z"]
          };
          
          const output = [];
          
          const build = (i, currStr, store) => {
              
              if (store.has(currStr)) return currStr;
              
              if (currStr.length === digits.length) {
                  store.add(currStr);
                  output.push(currStr);
                  return;
              }

              const letters = hash[digits[i]];
              
              for (letter of letters) {
                  build(i + 1, currStr + letter, store);
                  
              }
          }
          
          if (digits) {
              build(0, "", new Set())
          }
          
          return output;
      };
```

### [Remove Nth Node from end of list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
* This is a __singly linked list problem__
* It uses the __two pointer pattern__
* Make sure to declare a dummy node upfront
* Solution in javascript below
```javascript
    var removeNthFromEnd = function(head, n) {
        
        // dummy node is the node added before the head node, and has a null value.
        const dummyHead = new ListNode(null);
        dummyHead.next = head;

        let left = dummyHead;
        let right = head;
        // need to iterate through linked list to set the correct right pointer to the node at + n space apart
        while (right && n > 0) {
            right = right.next;
            n -= 1;
        }
        // classic linked list iteration, stop when right pointer is at null, i.e. just past the end
        while (right) {
            left = left.next;
            right = right.next;
        }
        
        // by setting left node pointer to the next.next node it will remove the node inthe middle.
        left.next = left.next.next;
        
        return dummyHead.next;
};
```
