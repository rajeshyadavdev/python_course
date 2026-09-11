""" 
This is used to control whether code should run directly or only when imported.

Synatx:
  if __name__ == "__main__":
    statement

1. Every Python file has a special variable called __name__.
2. If the file is run directly, __name__ becomes "__main__".
3. If the file is imported, __name__ becomes the module name.
4. This is useful for testing module code safely.
5. It prevents some code from running during import.

"""
def add(a,b):
  return a+b

if __name__ == "__main__":
  print(add(10,20))
  
# 30 

''' 
When running calculator.py directly: 30
When importing calculator.py into another file, the function is available, but the test print
does not run automatically.


Flow Chart
==========
Python file runs
|
v
Is file run directly?
|
├── Yes -> __name__ is "__main__"
|
└── No -> __name__ is module name
'''