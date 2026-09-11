""" 
The with statement is the recommended way to work with files.

Syntax
  with open("file_name", "mode") as file:
    statement

1. with automatically closes the file. It is safer than manually using close().
2. It works even if an error happens inside the block. It makes file handling cleaner.

"""
with open("data.txt","r",encoding="utf-8") as file:
  content = file.read()
  print(content)
  
''' 
No need to write:
file.close()
'''  