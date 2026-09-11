""" 
Variable shadowing happens when a local variable has the same name as a global variable.

Explanation:
    1. If a local and global variable have the same name, 
    Python uses the local variable inside the function.
    2. The global variable is not changed.
    3. This is called shadowing.


"""
name = "Global Aman"
def show_name():
    name = "Local Aman"  
    print(name) 
    
show_name()
print(name)  

# Local Aman
# Global Aman
  
  
# NOTE: Inside the function, the local variable gets priority over the global variable.