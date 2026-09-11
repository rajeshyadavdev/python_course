"""
Checking Python Version
-----------------------
The safest way is to download Python from the official Python website. The official Python
downloads page provides the latest stable Python release and installers for different
operating systems.

For Windows
-----------
1. Go to the official Python website.
2. Download the latest stable Python 3 installer.
3. Open the installer.
4. Select Add python.exe to PATH.
5. Click Install Now.
6. Wait for installation to complete.
7. Open Command Prompt and check the version.

Important: Always tick: Add python.exe to PATH
This option allows you to run Python from the terminal


For macOS
---------
Steps:
1. Download the macOS installer from the official Python website.
2. Open the .pkg file.
3. Follow the installation steps.
4. Open Terminal.
5. Check Python version.

Command: python3 --version


For Linux
---------
Many Linux systems already come with Python installed.
Check version: python3 --version
For Ubuntu/Debian-based systems, Python can usually be installed with:
sudo apt update
sudo apt install python3 python3-pip python3
"""
import platform
print("Installed Version Platform:", platform.python_version())

# Installed Version Platform: 3.12.8