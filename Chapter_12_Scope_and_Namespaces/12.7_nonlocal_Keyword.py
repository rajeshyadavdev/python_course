""" 
The nonlocal keyword is used to modify a variable from the nearest enclosing function
scope.

Syntax
    nonlocal variable_name

1. nonlocal is used inside nested functions. It allows the inner function to modify a
variable from the outer function.
2. It does not work with global variables.
3. The variable must already exist in the enclosing function. nonlocal is commonly used
in closures.
"""
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    inner()
outer()
# 1

# Without nonlocal
def outer():
    count = 0
    def inner():
        count += 1
        print(count)
    inner()
outer()
# UnboundLocalError: cannot access local variable 'count' where it is not associated with a value


# global vs nonlocal
''' 
Keyword     Used For                                Scope Affected
=======     ========                                ==============
global      Modify global variable                  Global scope
nonlocal    Modify enclosing function variable      Enclosing scope
Neither     Normal local variable                   Local scope

'''