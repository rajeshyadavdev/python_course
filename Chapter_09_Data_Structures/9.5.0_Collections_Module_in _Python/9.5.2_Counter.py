""" 
Counter is used to count how many times each value appears.

from collections import Counter
counter_name = Counter(iterable)

Explanation
  1. Counter counts repeated values.
  2. It returns a dictionary-like object.
  3. Items become keys.
  4. Their counts become values.
  5. It is commonly used for frequency counting.

Flow Chart
Input data
|
v
Counter checks each item
|
v
Counts repeated items
|
v
Returns item-count pairs
"""

from collections import Counter
letters = "banana"

counter = Counter(letters)
print(counter) # Counter({'a': 3, 'n': 2, 'b': 1})


# Example 2
items = ["apple", "banana", "apple", "mango", "banana", "apple"]
count = Counter(items)
print(count) # Counter({'apple': 3, 'banana': 2, 'mango': 1})


# Common Counter Methods
''' 
Method                Meaning                           Example
------                -------                           -------
most_common()         Returns most frequent items       count.most_common()
most_common(n)        Returns top n frequent items      count.most_common(2)
elements()            Returns items repeated by count   count.elements()
update()              Adds more counts                  count.update(data)
subtract()            Subtracts counts                  count.subtract(data)
'''
