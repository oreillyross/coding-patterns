# O(1)

def addition(num1, num2):
  
  num_iterations = 0
  
  total = num1 + num2
  num_iterations += 1
  
  print("The sum of %d and %d is %d" % (num1, num2, total))
  
# Not interested in steps, only iterations
# how do the iterations change in relation to the size of the input,
# This operation runs in constant time

# O(n)

def check_prime1(number):
  num_iterations = 0
  for i in range(2, number):
    num_iterations += 1
    
    if number % i == 0:
      print("%d is not a prime number, \nTotal number of iterations %d" % (number, num_iterations)
      return
   
  print("%d IS a prime number, \nTotal number of iterations %d" % (number, num_iterations)
        
 # input generalised to n is propotional to number of iterations
 # ignore constants
        
 
# O(n*n) or O(n^2)
# Usually nested for loops
        
def pairs(n,m):
        num_iters = 0
        for i in range(n):
          for j in range(m):
            num_iters += 1
     print(num_iters)
        
        

  
  
