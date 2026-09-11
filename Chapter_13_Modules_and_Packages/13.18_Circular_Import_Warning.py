""" 
A circular import happens when two modules import each other.

Example Structure
a.py imports b.py
b.py imports a.py

1. Circular imports can cause errors or incomplete imports.
2. They usually happen when modules depend on each other too much.
3. Good project structure helps avoid circular imports.
4. Shared code can be moved into a separate module.

Example Problem
a.py -> imports b.py
b.py -> imports a.py

Python may not finish loading one module before the other needs it.

Better Structure
common.py -> shared logic
a.py imports common.py
b.py imports common.py

"""