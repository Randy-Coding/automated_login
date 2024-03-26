from pywinauto import Desktop, Application
from pywinauto.keyboard import send_keys
import subprocess
import time
import keyring
from pywinauto import Desktop


def is_window_present():
    # This will go through all currently open windows and will locate the one that contains the title "1Password"
    # If it finds it, it will return true
    desktop = Desktop(backend="win32")
    window = desktop.window(title="1Password", visible_only=True)

    if window.exists(timeout=5):
        return True
    return False


def sign_in_with_1password(op_path):

    service_id = "1PasswordCLI"
    password_identifier = (
        "my1PasswordCLI" 
    )
    password = keyring.get_password(service_id, password_identifier)

    if not password:
        print(
            "Failed to retrieve password. Please visit do_this_first.py to set your password."
        )
        return

    # Start the 1Password CLI sign-in process as a subprocess
    subprocess.Popen([op_path, "signin"])

    # Sends the password if the window is found, and hits enter.
    if is_window_present():
        send_keys(f"{password}{{ENTER}}")


# Assuming a default op_path. Modify as needed.
op_path = r"C:\Program Files\1Password CLI\op.exe"

sign_in_with_1password(op_path)
