""" 
File modes tell Python how the file should be opened.

Mode      Meaning             File Must Exist?          Old Content
====      =======             ================          ===========
"r"       Read text file      Yes                       Not changed

"w"       Write text file     No                        Removed if file exists

"a"       Append text file    No                       Kept

"x"       Create new file     No                       Error if file exists

"b"       Binary mode         Depends                  Depends

"t"       Text mode           Depends                  Depends

"+"       Read and write      Depends                  Depends
"""

# Common Mode Combinations
''' 
Mode    Meaning
====    =======
"rt"    Read text file

"wt"    Write text file

"at"    Append text file

"rb"    Read binary file

"wb"    Write binary file

"r+"    Read and write existing file

"w+"    Write and read, overwrites file

"a+"    Append and read
'''
# Important point: Default mode is "rt", which means read text