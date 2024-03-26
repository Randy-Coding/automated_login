import keyring


# You will run this before anything else. If you do not have keyring installed you can type in pip install keyring and install it there.
# Type in the master password then hit enter, then after that you are ready to run the script_to_exe program.
service_id = "1PasswordCLI"
password_identifier = "my1PasswordCLI"

password = input("Enter your master password: ")
keyring.set_password(service_id, password_identifier, password)

print("Password stored securely. Please delete this python program")
