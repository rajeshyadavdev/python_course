""" 
asyncio is Python’s standard library module for asynchronous programming.

Syntax
import asyncio

1. asyncio runs asynchronous tasks.
2. It uses an event loop.
3. It is usually single-threaded cooperative concurrency.
4. Tasks pause when they reach await.
5. While one task is waiting, another task can run.


Flow Chart
==========
Event loop starts
|
v
Task 1 runs
|
v
Task 1 awaits
|
v
Task 2 runs
|
v
Tasks complete

"""