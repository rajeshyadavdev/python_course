""" 
Encoding decides how text is stored in bytes.

Syntex: 
  open("file.txt", "r", encoding="utf-8")

1. Text files store text using an encoding.
2. utf-8 supports most common characters.
3. Always mention encoding when working with text files.
4. Encoding problems can cause UnicodeDecodeError.

Example
=======
with open("data.txt", "w", encoding="utf-8") as file:
  file.write("Python is easy")
"""