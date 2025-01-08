class FibonacciIterator:
  def __init__(self, n):
    self.n = n
    self.index = 0
    self.a, self.b = 0,1

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= self.n:
      raise StopIteration
    if self.index == 0:
      self.index += 1
      return self.a
    elif self.index == 1:
      self.index += 1
      return self.b
    else:
      self.index += 1
      self.a, self.b = self.b, self.a + self.b
      return self.b

fib_iterator = FibonacciIterator(10)

print([next(fib_iterator) for _ in range(10)])
  