""" 
A common real-world example of a context manager is file handling.

Synatx:
  with open("data.txt","w") as file:
    file.write("Hello Python")
    

Explanation
1. open() returns a file object.
2. The file object works as a context manager.
3. The file opens at the start of the with block.
4. The file closes automatically at the end.
5. This is safer than manually closing the file.
"""