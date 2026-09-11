""" 
Keyword arguments pass values using parameter names.

Synatx:
   function_name(parameter_name=value)
   
1. Keyword arguments use names while calling a function.
2. Order does not matter when keyword arguments are used.
3. They make function calls more readable.
4. Positional arguments must come before keyword arguments.
   
"""

def student_info(name, age, course):
    print(f"Name:{name},Age:{age},Course:{course}")
    

student_info(course="Python",age=22,name="Rajesh")    
# Name:Rajesh,Age:22,Course:Python


# Positional vs Keyword Arguments
''' 
Type                    Example                                              Order Matters?
Positional argument     student_info("Aman", 21, "Python")                   Yes
Keyword argument        student_info(age=21, name="Aman",course="Python")    No
'''

# Important Rule

# Correct:
student_info("Ravi",course="Java",age=12)
# Name:Ravi,Age:12,Course:Java


# Incorrect:
# student_info(name="Ram",12,"C++")
# Positional argument cannot appear after keyword arguments


