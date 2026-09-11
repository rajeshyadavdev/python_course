""" 
Reading means getting data from a file.

Method        Meaning
======        =======
read()        Reads the entire file
readline()    Reads one line
readlines()   Reads all lines into a list
"""
file = open(file="data.txt",mode="r",encoding="utf-8")

# read()        Reads the entire file
entire_file = file.read()
print(entire_file)

file.close()

''' 
Hello Python
Welcome to file handling
'''