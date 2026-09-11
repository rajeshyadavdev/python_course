""" 
float means floating-point number. Float values contain decimal points.
They may be negative or positive

example:-
negative_mark = -2
positive_mark = 2

Python may display 99.50 as 99.5.

This does not mean the value is wrong. Python simply removes the unnecessary zero at the end.

"""

price = 100.23
height = 5.90
percentage = 87.60
temerature = -12.58

print(f"price:{price} and data type:{type(price)}")
print(f"height:{height} and data type:{type(height)}")
print(f"percentage:{percentage} and data type:{type(percentage)}")
print(f"temerature:{temerature} and data type:{type(temerature)}")
# price:100.23 and data type:<class 'float'>
# height:5.9 and data type:<class 'float'>
# percentage:87.6 and data type:<class 'float'>
# temerature:-12.58 and data type:<class 'float'>


# float() function convert int to float
int_value = 12
float_value = float(int_value)
print(f"Int value:{int_value} and data type:{type(int_value)}")
print(f"Float value:{float_value} and data type:{type(float_value)}")
# Int value:12 and data type:<class 'int'>
# Float value:12.0 and data type:<class 'float'>