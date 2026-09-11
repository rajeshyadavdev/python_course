"""
requirements.txt
----------------
requirements.txt is a file that stores the list of packages used in a Python project.
It helps other people install the same packages easily.

Example:
requests==2.32.3
pandas==2.2.2
numpy==2.0.1

Why requirements.txt is Important?
---------------------------------
Suppose you create a project and install many packages. Later, you share the project with
another person. Instead of telling them every package manually, you give them
requirements.txt. They can install everything using one command.

Create requirements.txt
After installing packages, run:
pip freeze > requirements.txt
or:
python -m pip freeze > requirements.txt

This creates a file like:
requests==2.32.3
urllib3==2.2.2
certifi==2024.7.4

Install Packages from requirements.txt
Use: pip install -r requirements.txt
or:
python -m pip install -r requirements.txt

Example Project Structure
weather_app/
│
├── app.py
├── requirements.txt
└── venv/


Commands:
  pip freeze > requirements.txt        for putting all package name into requirements.txt file
  pip install -r requirements.txt      for install all package from requirements.txt file
"""
print("requirements.txt keeps dependencies structured.")
