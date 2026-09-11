""" 
A coroutine is created using async def.

Syntax
  async def function_name():
    statement

Explanation
1. async def defines a coroutine function.
2. Calling a coroutine function returns a coroutine object.
3. The coroutine does not run immediately just because it is called.
4. It must be awaited or run by the event loop.
5. asyncio.run() is commonly used to start the main coroutine.
"""
import asyncio

async def greet():
  print("Hello World!")
 
asyncio.run(greet())  # Hello World!