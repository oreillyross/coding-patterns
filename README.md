# coding-patterns

✔️ = marked as easy

🚴‍♂️ = hard

🚩 = solved with two pointers 

🗃️ = Greedy Algorithm

♻️ = recursive solution

🔗 = Linked List


## Online tools to practice for technical interviews

* [Structy](https://structy.net/) This site offers a online playground along with course videos and explanations for practicing data structures and algorithms
* [TS Playground](https://www.typescriptlang.org/play?#code/Q) This is a good option for a technical interview if you have to code a solution to a problem using typescript.
* [Geeks for Geeks] (https://practice.geeksforgeeks.org/)
* [Interview Cake](https://www.interviewcake.com/)


## General Patterns to start solving a problem

* Start with Brute Force, even if you know it is not efficient it will lead to other considerations to solve the problem
* Keep track of the best answer so far in one pass of the problem, see if you can break it down into pieces
* Consider early to use a hash map, even if you don't know how yet as it is used in solving many problems generally.
* A depth first search of a graph uses a stack data structure behind the scenes
* A breadth first search of a graph uses a queue data structure behind the scenes

## Data Structures
### Trees
- know the difference between inorder (left, root, right), preorder (root, left, right) and postorder (left, right, root) traversal, this applies to depth-first searches. 

### Graphs

- Use for...in to get access to all keys if given a object with adjacency list to represent graph. For iterative inspection of each node.
- Use for...of to get the values of an object, so in this case it would be the adjacency list itself
- Know how to convert an edge list (array of pairs) into an adjacency list, which is an object with keys and values of arrays representing the connections

#### Cyle detection algorithm
- use the white-grey-black pattern (have a visting, visited Set()

#### Depth first traversal
- this can be done iteratively or recursively
- it uses a stack as the underlying data structure
- remember the adjacency list. Start with the node you have, passed in to function
- Iterative - stack.length > 0, pop from stack, for of into adjacency list, push onto stack
- Recursive - use node value, for of into G[node] adjacency list, recursively call function
- be careful of directed versus undirected graphs, undirected graphs need a way to stop cyclic calls, so add a visited feature.


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
- This problem can be solved using dynamic programming
- In an interview setting the easier option is to use the expand from middle technique and loop over the string (0(n^2) is best case
- The brute force solution is easiest to solve it but very poor performance n^3
- Be careful of the classic index +1 problem

### Roman to Integer challenge ✔️
 - This problem can be solved in a single for loop.
 - create a hash of the roman numerals to numbers first
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
