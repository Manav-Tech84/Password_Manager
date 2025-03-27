from cryptography.fernet import Fernet
#from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key","rb")
    keys = file.read()
    file.close()
    return keys

master_pwd = input("what is the master password ? ")
key = load_key() + master_pwd.encode()
fer: Fernet = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
      for line in f.readlines():
          data = line.rsplit("|")
          user,passw = data
          print("user:",user,"| password",
                fer.decrypt(passw.encode()).decode())


def add():
    name = input("User_Name: ")
    pwd  = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:

    mode = input("Would you like to add a new password or view existing ones(view,add), press q to quit ? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")