""" 
Syntax
  file.close()

1. Closing a file releases system resources. If a file is not closed, data may not be saved properly.
2. The with statement is preferred because it closes the file automatically.
"""
# Example 
file = open("data.txt", "r", encoding="utf-8")
file.close()