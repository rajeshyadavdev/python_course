""" 
await pauses a coroutine until an awaitable finishes.

Syntax
  await awaitable
  
Explanation
  1. await can be used only inside async def. It pauses the current coroutine.
  2. It allows the event loop to run other tasks.
  3. It is used with coroutines, tasks, and async operations.
"""

import asyncio

async def process():
  print("process started")
  
  await asyncio.sleep(1)
  
  print("process ended")
  
asyncio.run(process())  

''' 
process started
process ended
'''