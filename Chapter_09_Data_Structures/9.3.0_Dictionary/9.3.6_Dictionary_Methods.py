""" 
Dictionary methods are built-in operations used to access, update, remove, copy, and
manage dictionary data.

"""
# Assume this dictionary:
student = {
"name": "Aman",
"age": 21,
"course": "Python"
}

# keys() Returns all keys 
all_keys = student.keys() 
print(all_keys) # dict_keys(['name', 'age', 'course'])


# values() Returns all values 
all_values = student.values() 
print(all_values) # dict_values(['Aman', 21, 'Python'])


# items() Returns key-value pairs 
key_value_pairs = student.items()
print(key_value_pairs) # dict_items([('name', 'Aman'), ('age', 21), ('course', 'Python')])


# get() Returns value safely 
print(student.get("name") ) # Aman
print(student.get("city"))  # None  as city is not there in student


# update() Adds or updates data
student.update({"name":"Rajesh"})
print(student) # {'name': 'Rajesh', 'age': 21, 'course': 'Python'}


# pop() Removes key and returns value
pop_value = student.pop("course")
print(pop_value) # python


# popitem() Removes last inserted pairs

last_pair = student.popitem()
print(last_pair) # ('age', 21)


# clear() Removes all items 
student.clear() 
print(student) # {}


# copy() Creates shallow copy
person = {"name":"Rajesh","age":33,"type":"employee"}

new = person.copy()

new.update({"name":"Rakesh"})

print("old dict:",person) # old dict: {'name': 'Rajesh', 'age': 33, 'type': 'employee'}
print("new dict:",new) # new dict: {'name': 'Rakesh', 'age': 33, 'type': 'employee'}



# setdefault() Gets value or adds default

updated = person.setdefault(("city","Delhi"))
print(updated) # None
print(person) # {'name': 'Rajesh', 'age': 33, 'type': 'employee', ('city', 'Delhi'): None}



# fromkeys() Creates dictionary from keys

new_dict = dict.fromkeys(["age","name"],12)
print(new_dict) # {'age': 12, 'name': 12}


# Method Behavior Table
''' 
Method              Changes Original Dictionary?       Returns
------              ----------------------------       --------
keys()              No                                  View of keys
values()            No                                  View of values
items()             No                                  View of key-value pairs
get()               No                                  Value or default
update()            Yes                                 None
pop()               Yes                                 Removed value
popitem()           Yes                                 Removed key-value pair
clear()             Yes                                 None
copy()              No                                  New shallow copy
setdefault()        May change                          Existing/default value
fromkeys()          Creates new dictionary              New dictionary
'''








