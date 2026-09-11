""" 
Syntax:
if value:
    statement

Explanation
In Python, conditions do not always need direct comparison like: if age >= 18:
Python can also treat values as True or False. These are called truthy and falsy values.
A truthy value behaves like True. A falsy value behaves like False.


Common falsy values:
--------------------
False       => Boolean false
0           =>Zero number
0.0         =>Zero float
""          =>Empty string
None        =>No value


Common truthy values:
---------------------
True        =>Boolean true
10          =>Non-zero number
-5          =>Non-zero number
"Python"    =>Non-empty string
" "         =>String with a space


Important: " " is truthy because it contains a space. It is not empty.
"""

# Example 1: Non-empty string
name = "Rahul"
if name:
    print("Name is available")
else:
    print("Name is missing")
    
# Name is available


# Example 2: Empty string
name = ""
if name:
    print("Name is available")
else:
    print("Name is missing")
   
# Name is missing



# Example 3: Number
amount = 0
if amount:
    print("Amount available")
else:
    print("Amount is zero") 

# Amount is zero



#  