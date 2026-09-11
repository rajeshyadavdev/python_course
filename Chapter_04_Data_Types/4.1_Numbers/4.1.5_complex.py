""" 
complex numbers are numbers with two parts:
Real part + Imaginary part
In mathematics, complex numbers are usually written like this:
3 + 4i
But in Python, we use j instead of i.
"""
# Python complex number:
number = 3 + 4j
print(f"Complex Number:{number}, and data type:{type(number)}")
# Complex Number:(3+4j), and data type:<class 'complex'>

# Here: 3 = real part and 4j = imaginary part


# You can access real and imaginary parts like this

complex_number = 5 + 4j
print(f"complex number real-part:{complex_number.real} and imaginary-part:{complex_number.imag}")
# complex number real-part:5.0 and imaginary-part:4.0


# Python uses j for complex numbers, not i.

# Wrong 
# number = 4 + 6i

# Correct
number = 4 +6j