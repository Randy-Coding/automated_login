from pywinauto import Desktop, Application
from pywinauto.keyboard import send_keys
import subprocess
import time


from pywinauto import Desktop


def is_window_present():
    # This will go through all currently open windows and will locate the one that contains the title "1Password"
    # If it finds it, it will return true
    desktop = Desktop(backend="win32")
    window = desktop.window(title="1Password", visible_only=True)

    if window.exists(timeout=2):
        return True
    return False


def sign_in_with_1password(op_path, password):

    # Start the 1Password CLI sign-in process as a subprocess
    subprocess.Popen([op_path, "signin"])

    # Sends the password if the window is found, and hits enter.
    if is_window_present():
        send_keys(f"{password}{{ENTER}}")


# Assuming a default op_path. Modify as needed.
op_path = r"C:\Program Files\1Password CLI\op.exe"
password = "input_password"  # Replace this with the actual password or a secure retrieval method.

sign_in_with_1password(op_path, password)
