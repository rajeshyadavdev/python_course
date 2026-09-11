""" 
CSV means Comma-Separated Values. CSV files store table-like data.

Example CSV Data
================
name,age,course
Aman,21,Python

1. CSV files store rows and columns. Values are commonly separated by commas.
2. Python provides the built-in csv module. CSV is commonly used for spreadsheets and data export. 

Use newline="" when opening CSV files for writing.
"""

# Reading CSV File
import csv
with open("students.csv", "r",encoding="utf-8") as file:
  reader = csv.reader(file)

  for row in reader:
    print(row)
   
    
# Writing CSV File
with open("students.csv", "w",encoding="utf-8", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["name", "age", "course"])
  writer.writerow(["Aman", 21, "Python"])
