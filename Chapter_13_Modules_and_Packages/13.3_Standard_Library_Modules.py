""" 
The standard library is a collection of modules that come with Python. We do not need to
install them separately.

Explanation
  1. Standard library modules are built into Python.
  2. They help with math, dates, files, operating system tasks, random values, JSON, and more.
  3. We can use them by importing them
"""

# Common Standard Library Modules
''' 
Module          Purpose                         Example Use
=====           =======                         ===========
math            Mathematical operations         math.sqrt(25)
random          Random values                   random.randint(1, 10)
datetime        Date and time                   datetime.datetime.now()
os              Operating system tasks          os.getcwd()
sys             Python runtime information      sys.version
json            Work with JSON data             json.dumps(data)
statistics      Basic statistics                statistics.mean(data)
collections     Advanced data structures        Counter, deque
itertools       Iterator tools                  itertools.count()
pathlib         Work with file paths            Path("file.txt")

'''
import random
number = random.randint(1, 10)
print(number) 
# Output: A random number between 1 and 10
# Actual output changes every time because it is random.

