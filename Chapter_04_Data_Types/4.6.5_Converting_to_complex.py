""" 
complex() converts a value into a complex number.

"""
x = 5
y = complex(x)
print(f"x:{x},x-data-type:{type(x)} and y:{y},y-data-type:{type(y)}")
# x:5,x-data-type:<class 'int'> and y:(5+0j),y-data-type:<class 'complex'>


# String to complex:
m = "12"
n = complex(m)
print(f"m:{m},m-data-type:{type(m)} and n:{n},n-data-type:{type(n)}")
# m:12,m-data-type:<class 'str'> and n:(12+0j),n-data-type:<class 'complex'>

# but we cannot do like this p = "asd" q = complex(p) 
# we get error => ValueError: complex() arg is a malformed string