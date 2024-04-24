import subprocess
import sys
import os


def create_executable(py_file_path):
    try:
        # Optionally install PyInstaller if not installed
        # subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

        # Run PyInstaller to create the executable in the current directory
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "PyInstaller",
                "--onefile",
                "--distpath",
                ".",
                py_file_path,
            ]
        )
        print(
            f"Executable created successfully for {py_file_path} in the current directory"
        )

        # Construct the .spec file path to delete
        spec_file_path = os.path.splitext(py_file_path)[0] + ".spec"

        # Check if the .spec file exists and delete it
        if os.path.exists(spec_file_path):
            os.remove(spec_file_path)
            print(f"Deleted {spec_file_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error during the creation of the executable: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


create_executable("facial_recognition.py")
