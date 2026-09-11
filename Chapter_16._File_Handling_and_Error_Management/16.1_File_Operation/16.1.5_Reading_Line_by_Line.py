""" 
Reading line by line is useful for large files.

Syntax
  for line in file:
  statement

1. This reads one line at a time.
2. It is memory-friendly.
3. It is better than reading a very large file at once.
"""
with open(file="data.txt",mode="r",encoding="utf-8") as file:
  for line in file:
    print(line.strip())

''' 
Hello Python
Welcome to file handling
Here we are reding file line by line
'''    
# strip() removes extra newline characters from the line.
