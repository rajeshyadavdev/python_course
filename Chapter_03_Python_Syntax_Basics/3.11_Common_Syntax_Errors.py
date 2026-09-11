"""
Common Syntax Errors
--------------------

Syntax errors happen when Python cannot understand the code because syntax rules are
broken.

1. Missing Parentheses in print()
---------------------------------
Wrong:
PYTHON CODE
print "Hello"

Error: SyntaxError: Missing parentheses in call to 'print'

Correct:
PYTHON CODE
print("Hello")

2. Missing Colon
----------------
Wrong:
PYTHON CODE
age = 20

if age >= 18
print("Eligible")

Correct:
PYTHON CODE
age = 20
if age >= 18:
    print("Eligible")

A colon : is required after statements like: if, else, elif, for, while, def, class, try, except, finally

3. Wrong Indentation
--------------------
Wrong:
PYTHON CODE
if True:
print("Hello")

Correct:
PYTHON CODE
if True:
    print("Hello")

4. Using Keyword as Variable Name
---------------------------------
Wrong:
PYTHON CODE
for = 10

Correct:
PYTHON CODE
number = 10

5. Variable Used Before Assignment
----------------------------------
Wrong:
PYTHON CODE
print(name)
name = "Aman"

Error: NameError: name 'name' is not defined

Correct:
PYTHON CODE
name = "Aman"
print(name)
Python reads code from top to bottom. So the variable must be created before using it.


6. Missing Quotes Around String
-------------------------------
Wrong:
PYTHON CODE
name = Aman

Python thinks Aman is a variable.

Correct:
PYTHON CODE
name = "Aman"

7. Mismatched Quotes
--------------------
Wrong:
PYTHON CODE
message = "Hello Python'

Correct:
PYTHON CODE
message = "Hello Python"

Also correct:
PYTHON CODE
message = 'Hello Python'

8. Invalid Variable Name
------------------------
Wrong:
PYTHON CODE
student-name = "Nishchal"

Correct:
PYTHON CODE
student_name = "Nishchal"

9. Type Conversion Error
------------------------
Code:
PYTHON CODE
age = int(input("Enter your age: "))

If the user enters:
twenty

Python gives: ValueError: invalid literal for int()

Correct input should be numeric: 20

10. Unclosed Parentheses
------------------------
Wrong:
PYTHON CODE
print("Hello Python"

Correct:
PYTHON CODE
print("Hello Python")

11. Extra Closing Bracket
-------------------------
Wrong:
PYTHON CODE
print("Hello"))

Correct:
PYTHON CODE
print("Hello
"""
# Common issue: missing colon or unclosed parenthese
try:
    eval("if True print('error')")
except SyntaxError as e:
    print("Caught SyntaxError:", e)
