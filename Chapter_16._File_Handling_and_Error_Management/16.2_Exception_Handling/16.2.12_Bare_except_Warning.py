""" 
A bare except catches almost everything and should usually be avoided.

Bad Style
=========
try:
  number = int("abc")
except:
  print("Error")
  
Better Style
============
try:
  number = int("abc")
except ValueError:
  print("Invalid number")

Why Bare except is Bad ?

Problem                               Explanation
=======                               ===========
Too broad                             Catches errors you did not expect
Hides bugs                            Makes debugging difficult
Poor readability                      Does not show what error is handled
Can catch system-exit style errors    Not safe for normal us
"""