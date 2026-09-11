""" 
A return value is the result sent back by a function.

Syntax:
    def function_name():
        return value

1. return sends a value back to the place where the function was called.
2. A function can return one value or multiple values.
3. After return, the function stops executing.
4. If there is no return, Python returns None automatically.        

"""

def add(number1,number2):
    return number1 + number2


answer = add(10,20)
print(answer) # 30


# Example 2: Function without return
def greet():
    print("Hello World!")
    
result = greet()
print(result)  

# Hello World!
# None
  
# Because greet() does not return any value, Python returns None.