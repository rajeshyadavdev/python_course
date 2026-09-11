""" 
Feature         Threading               Multiprocessing               Asyncio
=======         =========               ===============               =======
Unit            Thread                  Process                       Coroutine/task
Memory          Shared                  Separate                      Shared in same thread
Best for        I/O-bound blocking work CPU-bound work                I/O-bound non-blocking work
Runs in         Same process            Separate processes            Event loop
Communication   Shared data, queue      Queue, pipe,manager           Awaitables, tasks
Main risk       Race conditions         Process overhead              Blocking the event loop
Common tool     threading               multiprocessing               asyncio

Important Async Rule
====================
Do not put long blocking code inside async functions.
If blocking code runs inside the event loop, it delays other async tasks. Python’s asyncio
development docs note that CPU-intensive work can block the event loop and delay other
tasks, and executors can be used to run such work elsewhere.

"""