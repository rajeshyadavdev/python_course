""" 
Async context managers are used with async with. They use:

__aenter__
__aexit__

not normal __enter__ and __exit__.

Syntax:

class ClassName:
  async def __aenter__(self):
    return self
    
  async def __aexit__(self, exc_type, exc_value, traceback):
    pass 
    
    
Explanation
1. async with is used for async resource management.
2. __aenter__ runs when the async context starts.
3. __aexit__ runs when the async context ends.
4. These methods can use await.
5. They are common in async database connections, HTTP clients, and network resources.
     
"""
import asyncio
class AsyncManager:
  async def __aenter__(self):
    print("Entering async context")
    return self
  async def __aexit__(self, exc_type, exc_value, traceback):
    print("Exiting async context")

async def main():
  async with AsyncManager():
    print("Inside async context")
      
asyncio.run(main())

''' 
Entering async context
Inside async context
Exiting async context
'''