"""
requirements.txt stores a list of packages needed for a project.

Syntax
  package_name==version


Example
requests==2.32.3
numpy==2.0.0

Task                      Command
====                      ======
Save installed packages   python -m pip freeze > requirements.txt
Install from file         python -m pip install -r requirements.txt


Explanation
1. requirements.txt helps share project dependencies.
2. Another user can install the same packages using one command.
3. It is commonly used in Python projects
"""