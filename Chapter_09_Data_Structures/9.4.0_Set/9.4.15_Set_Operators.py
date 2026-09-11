""" 
Set operations can also be done using operators.

Operator        Meaning                   Same As

`               `                         Union
&               Intersection              a.intersection(b)
-               Difference                a.difference(b)
^               Symmetric difference      a.symmetric_difference(b)
<=              Subset check              a.issubset(b)
<               Proper subset check       a < b
>=              Superset check            a.issuperset(b)
>               Proper superset check     a > b

"""