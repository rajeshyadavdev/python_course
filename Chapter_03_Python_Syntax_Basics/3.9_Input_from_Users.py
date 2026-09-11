"""
Input from Users
----------------
The input() function is used to take input from the user.

"""
name = input("Enter your name:")
print(f"Your name is {name}")

# Enter your name:Rajesh
# Your name is Rajesh



# Important Point
# The input() function always returns data as a string.

age = input("Enter your age:")
print(type(age))

# Enter your age:23
# <class 'str'>


# Even though the user entered 21, Python stores it as String "21".



# Taking Integer Input
# To convert input into an integer, use int().
mark = int(input("Enter your mark:"))
print(f"Your mark is {mark}")
print(type(mark))
# Enter your mark:54
# Your mark is 54
# <class 'int'>


# Taking Float Input
# To convert input into decimal number, use float().
price = float(input("Enter the amount of apple:"))
print(f"The price of mango is {price}")
print(type(price))

# Enter the amount of apple:234.34
# The price of mango is 234.34
# <class 'float'>



# If user enter floating point number and we want to convert to int then
# convert string to float then int
amount = int(float(input("Enter amount:")))
print(f"Your amount is {amount}")
print(type(amount))
# Enter amount:123.32
# Your amount is 123
# <class 'int'>



# What Happens Without int()?
first_number = input("Enter first number:")
second_number = input("Enter second number:")
sum = first_number + second_number
print(f"Sum of {first_number} and {second_number} is {sum}")
# Enter first number:10
# Enter second number:12
# Sum of 10 and 12 is 1012



# Here, Python joins the two strings. It does not perform mathematical addition because both values are strings.

# correct way to do sum
num1 = int(input("Enter number one:"))
num2 = int(input("Enter number two:"))
add = num1 + num2
print(f"Addition of {num1} and {num2} is {add}")
# Enter number one:10
# Enter number two:12
# Addition of 10 and 12 is 22