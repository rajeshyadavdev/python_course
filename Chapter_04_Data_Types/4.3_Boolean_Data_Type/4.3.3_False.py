""" 
False represents no, incorrect, inactive, unavailable, or disabled.

False  means  0

Important: False must start with capital F.
Correct: is_active = False
Wrong: is_active = false
Python uses False, not false.
"""
is_admin = False
is_expired = False
is_completed = False

print(is_admin,type(is_admin))
print(is_expired,type(is_expired))
print(is_expired,type(is_expired))
# False <class 'bool'>
# False <class 'bool'>
# False <class 'bool'>



print(True + True)  
# 2  why ? True = 1  so, 1 + 1 = 2

print(False + True)
# 1  why ? False = 0 and True = 1  so, 0 + 1 = 1

print(1+True)  # 2