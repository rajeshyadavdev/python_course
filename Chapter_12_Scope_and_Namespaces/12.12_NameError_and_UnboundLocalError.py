""" 
These errors are common in scope-related topics.

NameError
=========
NameError occurs when Python cannot find a name in LEGB search.
print(age)
Output: NameError: name 'age' is not defined


UnboundLocalError
=================
UnboundLocalError occurs when Python treats a variable as local because it is assigned
inside a function, but it is used before assignment.
x = 10
def show():
    print(x)
    x = 5
show()

output: UnboundLocalError: cannot access local variable 'x' where it is not associated with a value.
   
   
Error                Meaning
====                 =======
NameError            Name not found in any scope
UnboundLocalError    Local variable used before assignment
"""
