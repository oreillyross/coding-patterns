# Python has a built-in queue class

from queue import Queue

myqueue = Queue(5) # set iniital capacity

# all O(1)
myqueue.qsize() # return size
myqueue.put(2) # add an alement
myqueue.get() # first or next in the queue
myqueue.empty()
myqueue.full() # boolean if full or empty 

# Custom queue built using a list structure

class MyQueue:
  
  def __init__(self):
    # list DS under the hood
    self.items = []
  
  def is_empty(self):
    return len(items) == 0
  
  def enqueue(self, item):
    self.items.append(item)
    
  def dequeue(self):
    # simulate taking first item from list
    return self.items.pop(0)
  
  def size(self):
    return len(items)
  
  def peek(self):
    if self.is_empty():
      raise Exception("Nothing to peek")
    
    return self.items[0]
  
  
  
  




