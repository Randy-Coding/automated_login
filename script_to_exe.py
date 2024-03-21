import subprocess
import sys
import os

def create_executable(py_file_path):
    try:
        # Optionally install PyInstaller if not installed
        # subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
       
        # Run PyInstaller to create the executable in the current directory
        subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile",
                               "--distpath", ".", py_file_path])
        print(f"Executable created successfully for {py_file_path} in the current directory")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during the creation of the executable: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

create_executable('automate.py')