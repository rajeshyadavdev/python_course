""" 
str() converts a value into a string.


"""
age = 21

age_str = str(age)
print(f"age:{age},age-data-type:{age} and age-str:{age_str},age-str-data-type:{type(age_str)}")
# age:21,age-data-type:21 and age-str:21,age-str-data-type:<class 'str'>

# Important:
# After converting to str, the value becomes text.

x = 100
y = "100"
print(f"x-data-type:{type(x)} and y-data_type:{type(y)}")
# x-data-type:<class 'int'> and y-data_type:<class 'str'>