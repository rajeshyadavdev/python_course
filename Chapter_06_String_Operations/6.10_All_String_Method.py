# lower() Converts all characters to lowercase
text = "PYTHON"
print(text.lower()) # python


# upper() Converts all characters to uppercase 
text = "python"
print(text.upper()) # PYTHON


# title() Converts first letter of every word to uppercase
text = "python programming"
print(text.title()) # Python Programming


# capitalize() Capitalizes only the first letter of the string
text = "python programming"
print(text.capitalize()) # Python programming


# swapcase() Converts uppercase to lowercase and lowercase to uppercase

"""
strip() Removes spaces from both ends " Python ".strip() "Python"
lstrip() Removes spaces from the left side " Python".lstrip() "Python"
rstrip() Removes spaces from the right side "Python ".rstrip() "Python"
replace(old,
new)
Replaces one substring with another "I like
Java".replace("Java","Python")
"I like Python"
find() Returns the first index of a substring "Python".find("th") 2
index() Returns the index of a substring
(raises error if not found)
"Python".index("th") 2
count() Counts occurrences of a substring "banana".count("a") 3
startswith() Checks whether a string starts with a
substring
"Python".startswith("Py") True
endswith() Checks whether a string ends with a
substring
"Python".endswith("on") True
split() Splits a string into a list "a,b,c".split(",") ['a', 'b', 'c']
join() Joins iterable elements into a string "-".join(["A","B","C"]) "A-B-C"
isalpha() Returns True if all characters are
alphabets
"Python".isalpha() True
isdigit() Returns True if all characters are
digits
"12345".isdigit() True
isalnum() Returns True if all characters are
letters or digits
"Python3".isalnum() True
isspace() Returns True if all characters are
whitespace
" ".isspace() True
center(width) Centers the string within the specified
width
"Python".center(12) " Python "
zfill(width) Pads the string with leading zeros "25".zfill(5) "00025"

"""