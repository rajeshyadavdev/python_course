""" 
A lambda function is a small anonymous function. 
Anonymous means it does not need a normal function name.

Syntax:
  lambda arguments: expression

1. Lambda functions are used for small one-line functions.
2. They can take any number of arguments.
3. They can contain only one expression.
4. They automatically return the result of the expression.
5. Lambda functions are commonly used with map(), filter(), and sorting.


"""

# Normal function:

def square(number):
  return number * number

print(square(2)) # 4

# Same logic using lambda:

square = lambda number:number * number
print(square(5)) # 25

sum = lambda a,b:a+b
print(sum(12,11)) # 23

# Lambda is best for simple logic. For complex logic, use normal def functions.