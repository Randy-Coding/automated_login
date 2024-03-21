import subprocess
from pywinauto.keyboard import send_keys
import time


#This assumes a default op_path. If its somewhere else you have to specify.
op_path = r"C:\Program Files\1Password CLI\op.exe"
password = "input_password"

# Start the op sign-in process
proc = subprocess.Popen(
    [op_path, "signin"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

time.sleep(3)
send_keys(password + "{ENTER}")
