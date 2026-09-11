""" 
A variable is like a name tag.

It points to a value.
Example: 
x = 10 Means x -----> 10

Now: 
x = 20 Means x -----> 20

The name x now points to 20. It does not mean 10 changed into 20.
This idea is very useful for understanding mutable and immutable data later.

"""

x = 10
print(f"Val: {x}, Address: {id(x)}") #Val: 10, Address: 140713904630488
x += 1
print(f"Updated Val: {x}, New Address: {id(x)}") # Updated Val: 11, New Address: 140713904630520

