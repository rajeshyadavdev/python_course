# Merging means combining two or more dictionaries.

student = {"name":"Rajesh","age":22}
extra = {"course":"python","city":"Delhi"}

student.update(extra)

print(student) #{'name': 'Rajesh', 'age': 22, 'course': 'python', 'city': 'Delhi'}


# Example 2: Using |
person = {"name":"Rajesh","age":23}
more = {"type":"employee","city":"Bihar"}
result = person | more
print(result) # {'name': 'Rajesh', 'age': 23, 'type': 'employee', 'city': 'Bihar'}




# Same Key During Merge
# If both dictionaries have the same key, the second dictionary value wins.
a = {"name": "Kaavya", "age": 21}
b = {"age": 22, "course": "Python"}
result = a | b
print(result) # {'name': 'Kaavya', 'age': 22, 'course': 'Python'}


