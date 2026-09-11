""" 
float() converts a value into a decimal number.

"""

x = "10.22"
y = float(x)
print(f"x:{x},x-data-type:{type(x)} and y:{y}, and y-data-type:{type(y)}")
# x:10.22,x-data-type:<class 'str'> and y:10.22, and y-data-type:<class 'float'>

# Integer to float:
p = 10
q = float(p)
print(f"p:{p},p-data-type:{type(p)} and q:{q},q-data-type:{type(q)}")

# p:10,p-data-type:<class 'int'> and q:10.0,q-data-type:<class 'float'>


# String integer to float:
m = "100"
n = float(m)
print(f"m:{m},m-data-type:{type(m)} and n:{n},m-data-type:{type(n)}")
# m:100,m-data-type:<class 'str'> and n:100.0,m-data-type:<class 'float'>


# Invalid conversion:

value = "python"
float_value = float(value)
# ValueError: could not convert string to float: 'python'