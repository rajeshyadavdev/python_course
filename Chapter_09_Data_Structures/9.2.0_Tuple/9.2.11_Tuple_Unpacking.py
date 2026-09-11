""" 
Syntax:
  var1, var2, var3 = tuple_name

Explanation
  1. Tuple unpacking means taking values from a tuple and storing them in separate
    variables.
  2. The number of variables should match the number of tuple values.
  3. Unpacking makes code cleaner and readable.
"""
student = ("Rajesh",25,"python")
name, age, course = student
print(f"name {name},age {age} and course {course}")
# name Rajesh,age 25 and course python


# Important Point
student = ("Aman", 21, "Python")
name, age = student # ValueError: too many values to unpack (expected 2)

# Because the tuple has 3 values, but only 2 variables are given.


