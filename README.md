# coding-patterns to help as an aide-memoire



## Online tools to practice for technical interviews

* [Structy](https://structy.net/) This site offers a online playground along with course videos and explanations for practicing data structures and algorithms
* [TS Playground](https://www.typescriptlang.org/play?#code/Q) This is a good option for a technical interview if you have to code a solution to a problem using typescript.
* [Geeks for Geeks] (https://practice.geeksforgeeks.org/)
* [Interview Cake](https://www.interviewcake.com/)
* [Leet code](https://leetcode.com/)
* [Neet code](https://www.youtube.com/channel/UC_mYaQAE6-71rjSN6CeCA-g) A youtube channel from a a guy who is now a Google engineer who created videos in python of many Leet code challenges


## General Patterns to start solving a problem

* Start with Brute Force, even if you know it is not efficient it will lead to other considerations to solve the problem
* Keep track of the best answer so far in one pass of the problem, see if you can break it down into pieces
* Consider early to use a hash map, even if you don't know how yet as it is used in solving many problems generally.
* A depth first search of a graph uses a stack data structure behind the scenes
* A breadth first search of a graph uses a queue data structure behind the scenes


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


### Backtracking
* This is common in problems which require a bruteforce approach. 
* Think of the problem in terms of a decision tree which branches out exponentially, i.e. based on the number of inputs
* upon reaching the leaf nodes you can _backtrack_ up the tree to the root node to get each and every variation.
* problems solved with this approach include the [Letter Combinations](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) problem from Leetcode.
* use a recursive function inside your main function to build the result recursively.
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
 * The algorithm requires two functions, one which takes two sorted arrays and returns one osrted array, a second function which recursively divides arrays.
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
 - The precondition to searching is that the array must be sorted.
 - Key pieces are two pointers, one initially pointing to the first value (low pointer), the other pointing to the end of the array (high pointer).
 - algorithmic step is to find the midpoint (floored for whole number), check if it matches the target value, or if its lower than target value, move low pointer 
 to the midpoint index, if its higher, move the high pointer to the mid point index, repeat until target found or low matches high index. Then no match.
 
     //while the two pointers dont cross
      //find midpoint index
      // check if target higher, move low pointer to midpoint + 1
      // if target lower move high pointer to mid - 1 
      // else it is equal to mid, reutnr mid as its the index
  
      //all else fails return -1



### Topological order
- Key to victory is to build a hash map of the parents and their connections, so numParents = {};
- Also have an array called ready, which takes the nodes that have a count of 0 in the numParents object
- Add the last node in ready to the order array, return this order array as the final result. 

## Data Structures

### Trees
- know the difference between inorder (left, root, right), preorder (root, left, right) and postorder (left, right, root) traversal, this applies to depth-first searches. 

#### Binary tree


### [Lefty nodes problem](https://structy.net/problems/premium/lefty-nodes)
- Start with a helper function that takes a node, and a count of what level you are on
- put the helper function inside the main function to make use of the closure behaviour of javascript to get access to the returned values array.
- inside the helper function recursively call itself passing in the left and then the right nodes, and level + 1.
- the base case is if node is null and you push a value if values.length === level.



# Graphs

* Use <code>for ... in</code> to get access to all keys if given a object with adjacency list to represent graph. For iterative inspection of each node.
* Use <code>for ... of</code> to get the values of an object, so in this case it would be the adjacency list itself
* Know how to convert an edge list (array of pairs) into an adjacency list, which is an object with keys and values of arrays representing the connections.
### <em>edge list to adjacency list</em>
- create helper function buildGraph, pass in edge list (array of sub arrays)
- create empty graph object, rturn it at the end
- iterate (<code>for ... of</code>) through every sub array
- destructure the pairs of each sub array
- add each destructured item to the graph object if not in the graph, initialise it as an empty adjacency array.
* undirected graph -> push both items into each other's arrays.
* directed graph -> push only the second item into first array.


## Cyle detection algorithm
- use the white-grey-black pattern (have a visting, visited Set()

## <p style="color: lightgreen">Depth first traversal</p>
- this can be done iteratively or recursively
- it uses a stack as the underlying data structure
- remember the adjacency list. Start with the node you have, passed in to function
- Iterative - stack.length > 0, pop from stack, for of into adjacency list, push onto stack
- Recursive - use node value, for of into G[node] adjacency list, recursively call function
- be careful of directed versus undirected graphs, undirected graphs need a way to stop cyclic calls, so add a visited feature.

## <p style="color: lightgreen">Island hopping logic</p>
  - You will need a graph in the form of an object where the keys are nodes and the values are adjacency lists.
  - You get access to the adjacency lists and are inclusive of all islands by using the <code>for ... in call</code> on the graph.

## <p style="color: lightgreen">Bipartite graphs and graph coloring</p>

<hr/>

# Dynamic Programming patterns

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