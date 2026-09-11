""" 
Method          Purpose               Example                           Result / Effect
add()           Adds one item         s.add(10)                         Adds 10
update()        Adds multiple items   s.update([10, 20])                Adds all items
remove() Removes item s.remove(10) Error if missing
discard() Removes item safely s.discard(10) No error if missing
pop() Removes random item s.pop() Returns removed item
clear() Removes all items s.clear() Empty set
copy() Creates shallow copy new = s.copy() New set
union() Combines sets a.union(b) New set
intersection() Common items a.intersection(b) New set
difference() Items in first but not second a.difference(b) New set
symmetric_differe
nce()
Items not common a.symmetric_difference(b) New set
intersection_updat
e()
Keeps only common items a.intersection_update(b) Changes a
difference_update(
)
Removes items found in other
set
a.difference_update(b) Changes a
symmetric_differe
nce_update()
Keeps non-common items a.symmetric_difference_u
pdate(b)
Changes a
issubset() Checks subset a.issubset(b) True/False
issuperset() Checks superset a.issuperset(b) True/False
isdisjoint() Checks no common items a.isdisjoint(b) True/False
"""