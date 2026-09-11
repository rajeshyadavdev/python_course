"""
Basic Program Structure
-----------------------
A basic Python program usually follows this flow:

Start
|
v
Take input / define data
|
v
Process data
|
v
Display output
|
v
End
"""

name = input("Enter Student name:")

mark_in_science = int(input("Enter marks of science:"))
mark_in_math = int(input("Enter marks of math:"))
mark_in_sst = int(input("Enter marks of sst:"))

message = f"{name} marks in science: {mark_in_science},math: {mark_in_math} and sst: {mark_in_sst}"

total_mark = mark_in_science + mark_in_math + mark_in_sst
avearage_mark = total_mark/3

print(message)
print(f"Total marks:{total_mark}")
print(f"Average Mark :{avearage_mark}")


# Enter Student name:Rajesh
# Enter marks of science:89
# Enter marks of math:80
# Enter marks of sst:89
# Rajesh marks in science: 89,math: 80 and sst: 89
# Total marks:258
# Average Mark :86.0