""" 
Function annotations are used to add type hints to function parameters and return values.

Synatx:
    def function_name(parameter: type) -> return_type:
        statement
        
1. Function annotations describe expected data types. They make code easier to understand.
2. They help editors and tools detect possible mistakes.
3. Python does not automatically enforce these types at runtime.
4. Annotations are stored in the function’s __annotations__ attribute.

        
"""
def sum_of_number(a:int,b:int)->int:
    return a + b

print(sum_of_number(12,12)) # 24
print(sum_of_number.__annotations__) 
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# Important point: Type hints are hints. Python does not stop wrong types automatically.
