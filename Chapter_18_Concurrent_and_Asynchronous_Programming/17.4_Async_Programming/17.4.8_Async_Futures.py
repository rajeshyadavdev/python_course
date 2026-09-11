""" 
An asyncio.Future represents a result that may be available later.
1. asyncio.Future is a low-level awaitable object.
2. It is mainly used inside asyncio libraries and frameworks.
3. In normal application code, prefer coroutines and tasks.
4. Do not confuse asyncio.Future with concurrent.futures.Future.


Python’s docs note that asyncio.Future is usually for low-level callback-based code and recommend not exposing Future objects in user-facing APIs.


Future Comparison
=================
Type                        Module                    Used With
----                        ------                    ---------
concurrent.futures.Future   concurrent.futures        Thread/process executors
asyncio.Future              asyncio                   Event loop and async tasks

"""
