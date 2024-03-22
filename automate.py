from pywinauto import Desktop, Application
from pywinauto.keyboard import send_keys
import subprocess
import time


def sign_in_with_1password(op_path, password):
    try:
        # Start the 1Password CLI sign-in process as a subprocess
        subprocess.Popen([op_path, "signin"])

        time.sleep(2)
        desktop = Desktop(backend="uia")

        # Now connect to the window of 1Password using pywinauto
        # Replace 'Title_of_the_window' with the actual title if it's available
        # Since the window may not have the title '1Password', you might need to
        # use another attribute for the window specification, like control_id or automation_id
        candidate_windows = [
            w for w in desktop.windows() if "1Password" in w.window_text()
        ]

        # Next, refine the search among the candidate windows for a specific text
        for w in candidate_windows:
            if "Enter your password" in w.window_text():
                dialog = w
                break

        if dialog is not None:
            send_keys(password + "{ENTER}")
            print("Password entry and authorization attempt made.")
        else:
            print("The 1Password sign-in window did not appear.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Assuming a default op_path. Modify as needed.
op_path = r"C:\Program Files\1Password CLI\op.exe"
password = "input_password"  # Replace this with the actual password or a secure retrieval method.

sign_in_with_1password(op_path, password)
