""" 
True represents yes, correct, active, available, or enabled.

True   means 1


Important: True must start with capital T.
Correct: is_active = True
Wrong: is_active = true
Python will not understand true because Python uses True.

"""

is_logged_in = True
is_active = True
is_deleted = False
print(is_logged_in,type(is_logged_in))
print(is_active,type(is_active))
print(is_deleted,type(is_deleted))

# True <class 'bool'>
# True <class 'bool'>
# False <class 'bool'>

print(True + True)  
# 2  why ? True = 1  so, 1 + 1 = 2

print(False + True)
# 1  why ? False = 0 and True = 1  so, 0 + 1 = 1

print(1+True)  # 2
