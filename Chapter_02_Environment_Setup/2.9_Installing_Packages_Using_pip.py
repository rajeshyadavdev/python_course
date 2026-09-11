"""
Installing Packages Using pip
-----------------------------
pip is Python’s package installer. It is used to install external libraries.

Python’s official installing guide describes PyPI as a public repository of open-source
packages, and pip is used to install packages from it.

What is a Package?
------------------
A package is reusable code created by someone else.Instead of writing everything from
scratch, we can install packages.

Command: pip install package_name
Example: pip install requests
Better command: python -m pip install requests

Why python -m pip is Better?
----------------------------
This makes sure pip installs the package for the same Python interpreter you are using. This
is helpful when multiple Python versions are installed.

List Installed Packages
pip list or: python -m pip list
"""
print("pip is the standard package installer for Python.")
