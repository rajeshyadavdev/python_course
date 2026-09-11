""" 
set_name.remove(value)
set_name.discard(value)
set_name.pop()
set_name.clear()

1. remove() removes a specific item.
2. discard() also removes a specific item.
3. pop() removes a random item because sets are unordered.
4. clear() removes all items.

"""
numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers) # {40, 10, 30}

numbers.discard(50)
print(numbers) # {40, 10, 30}
# discard(50) does not give an error even though 50 is missing.



''' 
Removing Methods Table
======================
Method          Purpose                         If Value Missing
------          -------                         ----------------
remove(value)   Removes specific value          Gives KeyError
discard(value)  Removes specific value          No error
pop()           Removes random item             Gives error if set is empty
clear()         Removes all items               No error
'''