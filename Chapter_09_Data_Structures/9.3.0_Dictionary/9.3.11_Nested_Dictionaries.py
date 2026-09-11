""" 
Synatx:
nested_dictionary ={
  key_1:{
    key_1:value_1,
    key_2:value_2
  },
  key_2:{
    key_1:value_1,
    key_2:value_2
  }
}

Explanation
  1. A nested dictionary means a dictionary inside another dictionary.
  2. It is useful for storing structured data.
  3. To access inner values, use multiple keys.
  4. Nested dictionaries are common in real-world data like users, students, products, and
    API responses.

"""
students = {
"student1": {
"name": "Rakesh",
"age": 21
},
"student2": {
"name": "Rajesh",
"age": 22
}
}

print(students["student1"]["name"]) # Rakesh
print(students["student2"]["age"])  # 22

print(students.get("student1").get("name"))  # Rakesh
print(students.get("student2").get("age"))   # 22


# Updating Nested Dictionary
students["student1"]["age"] = 20

print(students["student1"]) # {'name': 'Rakesh', 'age': 20}

