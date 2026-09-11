""" 
The global keyword is used to modify a global variable inside a function.

Syntax
    global variable_name

Explanation
    1. Use global when you want to assign a new value to a global variable inside a
    function.
    2. Without global, assignment inside a function creates a local variable.
    3. Reading a global variable does not need global. Using too many global variables is
    not recommended.
    
"""
count = 0
def increase_count():
    global count
    count +=1
    
increase_count()    
print(count) # 1


# Without global
c = 3
def decrease_count():
    c -= 1
    
# decrease_count()
#UnboundLocalError: cannot access local variable 'c' where it is not associated with a value  
  
print(c)    


# NOTE: Use global only when you really need to modify a global variable. 
# Better style is usually to return a value:
def increase_count(count):
    return count + 1

count = 0
count = increase_count(count)
print(count) # 1


