# coding-patterns

## General Patterns to start solving a problem

* Start with Brute Force, even if you know it is not efficient it will lead to other considerations to solve the problem
* Keeo track of the bwest answer so far in one pass of the problem, see if you can break it down into pieces
* Consider early to use a hash map, even if you don't know how yet as it is used in solving many problems generally.

### 0 1 1 2 3 5 8 problem

- The key to this is to remember that you need to start with two numbers you already know. Otherwise you have nothing to add. 
- The recursive solution is WAAAY to ineficient, and a simple 0(n) for loop where you store the result in an array thus building up the Fibbonaci sequence.
- If you do use a recursive solution, definitely make sure you use memoization strategy, :hammer:
- If you want to look clever (or dumb) pull out Benet's formula to calculate the Fibonacci sequence.

### Two sums problem 
 - The brute force approach suggests two for loops giving 0(n2)
 - the introduction of a hash or map allows one to capture the value as the key in the kv store which later can be checked if the complement (i.e. the difference) between target value and the value being iterated.
 - This can be done in one pass, if the checks for equality are done before the hash map is further constructed. :fire:

### Reverse words in a string
- Without using any of the ES5+ javascript functions such as split, filter, reverse and join one can create two for loops (2n) and construct the reversed words
- space requirements include two arrays
- an improvement would include starting at the back of the string and repeating same first for loop to end up with words reversed on the first iteration

### Add two numbers
- This problem expects you to know singly linked lists. 
- Store a reference to the current (dummy) linked list so you can get to it after the while loop terminates 💥
- It has a numbe of edgecases which can make it tricky. Remember the two input linked lists can be different lengths
- The trickiest edge case is remembering at the end there might be a digit to carry over which needs to be added to Linked List which is returned.

### Longest Palindromic substring
- This problem can be solved using dynamic programming
- In an interview setting the easier option is to use the expand from middle technique and loop over the string (0(n^2) is best case
- The brute force solution is easiest to solve it but very poor performance n^3
- Be careful of the classic index +1 problem
