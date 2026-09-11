""" 
The event loop manages and runs async tasks.
1. The event loop schedules coroutines. It switches between tasks when they await.
2. asyncio.run() creates and manages the event loop for most programs.
3. Beginners should usually use asyncio.run() instead of manually creating loops.


"""