# unpacking a sequence into separate variables
# Works with any objects that happen to be iterable
p = (4, 5)
x, y = p

print(x)
print(y)

s = 'Hello'
a,_,b,_,_ = s
print(a,b)

# Unpacking elements form iterables of arbitrary length
# Use the str expression to represent multiple elements to be ignored. Use the sytnax *_ to ignore and thorw away multiple elements.



def drop_first_last(grades):
  first, *middle, last = grades
  return sum(middle)/len(middle)

grades = [1,2,3,2,5,6]
print(drop_first_last(grades))

line = 'nobody:*:-2:-2:Unpriviliged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)

# Keeping the last N Items
# Using the deque with maxlen defined makes a kind of history datastructure, where the oldest itmes added are automatically popleft() off the queue as new items are appended from the right.

from collections import deque

def search(lines, pattern, history=5):
  previous_lines = deque(maxlen=history)
  for line in lines:
    if pattern in line:
      yield line, previous_lines
    previous_lines.append(line)

if __name__ == '__main__':
  with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
      for pline in prevlines:
        print(pline, end='')
      print(line, end='')
      print('-'*20)

# Finding the largest of smallest N items

