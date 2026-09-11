""" 
A task schedules a coroutine to run concurrently.

Syntax
  task = asyncio.create_task(coroutine())

1. A task wraps a coroutine. It schedules the coroutine to run on the event loop.
2. Multiple tasks can run concurrently. await task gets the final result.

"""
import asyncio

async def work(name):
  await asyncio.sleep(1)
  print(name, "done")

async def main():
  task1 = asyncio.create_task(work("Task 1"))
  task2 = asyncio.create_task(work("Task 2"))

  await task1
  await task2

asyncio.run(main())

''' 
Task 1 done
Task 2 done
'''
# Both tasks wait concurrently.
