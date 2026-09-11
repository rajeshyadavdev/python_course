""" 
Synatx:
  set_name.add(value)
  set_name.update(iterable)
  
  
Explanation
1. add() adds one item.
2. update() adds multiple items.
3. If an added value already exists, it is not added again.
4. Sets automatically maintain uniqueness.
"""

numbers = {10, 20, 30}
numbers.add(40)
print(numbers) # {40, 10, 20, 30}

numbers.update([100,20,300])
print(numbers) # {100, 40, 10, 300, 20, 30}

# 20 was already present, so it is not duplicated.


''' 
add() vs update()
-----------------
Method            Adds                Example
------            ----                -------
add()             One item            items.add(10)
update()          Multiple items      items.update([10, 20])
'''