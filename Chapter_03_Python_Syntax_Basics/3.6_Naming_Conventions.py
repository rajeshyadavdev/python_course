"""
Naming Conventions (PEP 8)
--------------------------
Variable names should be meaningful and easy to understand.

snake_case for variables and functions
--------------------------------------
first_name = "Rajesh" 
def add_number():
    return 10+20

PascalCase for classes
----------------------
class StudentModel:
    pass

UPPER_CASE for constants
------------------------
PI = 3.143

"""

# Good variable names:
user_age = 25  # snake_case
is_logged_in = True # snake_case
MAX_RETRIES = 5  # UPPER_CASE


# Bad variable names:
x = 12
tm = 89
flag = True

# These names are not always wrong, but they are less clear.



# Rules for Naming Variables
''' 
Variable name can contain letters          
eg. marks = 89 (correct)
eg. #marks = 89 (wrong)  variable name cannot contain # 

Variable name can contain numbers          
eg. student1 = "Rajesh" (corect)
eg. 1student = "Rajesh" (wrong)  variable name cannot start with number

Variable name can contain underscore _     
eg. student_name = "Aman"  (correct)
eg. student$name = "Aman"  (wrong) variable name cannot contain special character except underscore

Variable name cannot contain spaces        
eg. total_marks = 90 (correct)
eg. total marks = 90 (wrong)  variable name cannot contain space

Variable name cannot use keywords 
eg. course_name = "Python" (correct)
eg. class = "Java" (wrong)  variable name cannot be used keywods as class is keyword

Variable name are Case-sensitive 
eg. name = "Amar", Name = "Amar"

'''

# Valid variable names:
age = 30
first_name = "Rajesh"
_total = 343
is_active = True

# Invalde variable name
# 1name = "Aman"   variable name cannot start with number
# first-name = "Raju"  variable name cannot contain any special character except underscore
# total mark = 45   variable name cannot contain space
# class = "ten"  variable name cannot used as keywords