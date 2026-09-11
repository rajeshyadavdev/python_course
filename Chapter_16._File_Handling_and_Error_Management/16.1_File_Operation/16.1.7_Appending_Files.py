""" 
Appending means adding new data at the end of an existing file.

Syntax
 open("file_name", "a")

Explanation
1. "a" means append mode. New data is added at the end.
2. Old content is not removed. If the file does not exist, Python creates it.
"""
with open(file="data.txt",mode="a",encoding="utf-8") as file:
  file.write("\nAppending into file")

''' 
Welcome to python coding.
Appending into file


Here file line was already there now added second line.
'''