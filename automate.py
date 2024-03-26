from pywinauto import Desktop, Application
from pywinauto.keyboard import send_keys
import subprocess
import time


from pywinauto import Desktop


def is_window_present():
    desktop = Desktop(backend="win32")
    window = desktop.window(title="1Password", visible_only=True)

    if window.exists(timeout=5):
        return True
    return False


def sign_in_with_1password(op_path, password):

    # Start the 1Password CLI sign-in process as a subprocess
    subprocess.Popen([op_path, "signin"])

    if is_window_present():
        send_keys(password)


# Assuming a default op_path. Modify as needed.
op_path = r"C:\Program Files\1Password CLI\op.exe"
password = "input_password"  # Replace this with the actual password or a secure retrieval method.

sign_in_with_1password(op_path, password)
