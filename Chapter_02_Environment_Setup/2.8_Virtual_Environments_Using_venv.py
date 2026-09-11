"""
Virtual Environments Using venv
-------------------------------
A virtual environment is an isolated environment for a Python project. It keeps project
packages separate from other projects.

Python’s official documentation says venv is the standard tool for creating virtual
environments, and each virtual environment has its own independent set of installed Python
packages.

Why Virtual Environment is Needed?
----------------------------------
Suppose you have two projects:
Project A needs package version 1.0
Project B needs package version 2.0
If both projects use the same global Python environment, package conflicts can happen.

Virtual environments solve this problem.
Computer Python
↓
Project A → venv → packages for Project A
Project B → venv → packages for Project B
Project C → venv → packages for Project C


Commands:
  python -m venv myenv
  myenv\Scripts\activate (Windows)
  source myenv/bin/activate (Linux/Mac)
"""
import sys
print("prefix:",sys.prefix) 
#prefix: C:\Users\Admin\AppData\Local\Programs\Python\Python312

print("base_prefix:",sys.base_prefix) 
# base_prefix: C:\Users\Admin\AppData\Local\Programs\Python\Python312

print("In virtual environment:", sys.prefix != sys.base_prefix) # False
