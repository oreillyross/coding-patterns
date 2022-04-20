/*
  A heap is a data structure which resembles a tree that is mostly balanced
  This gives one the ability to have fast inserts at O(log n) and fast deletes
  and because you only take the root of the tree, you can also have fast
  searches at O(1) time.
  In a min-heap, the root is the smallest element in the tree.
  In a max-heap, the root is the largest element in the tree.
  Every node obeys the heap property, which means that every node is either
  smaller than its children or larger than its children.
  In order to maintain this balance there are two important functions that a heap 
  needs namely bubble up and bubble down. 

  Bubble up: 
  This function takes a node and moves it up the tree until it obeys the heap property.
  This is done by comparing the node with its parent and swapping them if the parent is
  larger than the child.
  Bubble down:
  This function takes a node and moves it down the tree until it obeys the heap property.
  This is done by comparing the node with its children and swapping them if the child is
  larger than the parent.
  
  Other common methods on the heap class include, peek, size, isEmpty, insert, remove

*/

class Heap {
	
	constructor() {
		this.heap = [];
	}

	// Returns the size of the heap
	size() {
		return this.heap.length;
	}

	// Returns true if the heap is empty
	isEmpty() {
		return this.size() === 0;
	}

	// Returns the root of the heap
	peek() {

		if (this.isEmpty()) {
			return null;
		}

		return this.heap[0];
	}

	// Inserts a new element into the heap
	insert(element) {
		
		this.heap.push(element);
		this.bubbleUp(this.size() - 1);
	}

	// Removes the root of the heap
	remove() {
		
		if (this.isEmpty()) {
			return null;
		}

		let root = this.heap[0];
		let last = this.heap.pop();

		if (!this.isEmpty()) {
			this.heap[0] = last;
			this.bubbleDown(0);
		}

		return root;
	}

	// Bubbles up the element at the given index
	bubbleUp(index) {
		
		let parent = this.getParent(index);

		while (index > 0 && this.heap[index] < this.heap[parent]) {
			this.swap(index, parent);
			index = parent;
			parent = this.getParent(index);
		}
	}

	// Bubbles down the element at the given index
	bubbleDown(index) {
	
		let left = this.getLeftChild(index);
		let right = this.getRightChild(index);
		let smallest = index;

		if (left < this.size() && this.heap[left] < this.heap[index]) {
			smallest = left;
		}

		if (right < this.size() && this.heap[right] < this.heap[smallest]) {
			smallest = right;
		}

		if (smallest !== index) {
			this.swap(index, smallest);
			this.bubbleDown(smallest);
		}
	}

	// Swaps the elements at the given indices
	swap(index1, index2) {
		
		let temp = this.heap[index1];
		this.heap[index1] = this.heap[index2];
		this.heap[index2] = temp;
	}

	// Returns the index of the parent of the element at the given index
	getParent(index) {
		return Math.floor((index - 1) / 2);
	}

	// Returns the index of the left child of the element at the given index
	getLeftChild(index) {
		return 2 * index + 1;
	}

	// Returns the index of the right child of the element at the given index
	getRightChild(index) {
		return 2 * index + 2;
	}

	// Returns a string representation of the heap
	toString() {
		return this.heap.toString();
	}


}

export { Heap };
