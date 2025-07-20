from cryptography.fernet import Fernet

# Uncomment this and run once to generate the key file
#def write_key():
 #   key = Fernet.generate_key()
  #  with open("key.key", "wb") as key_file:
  #   key_file.write(key)
#write_key()


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.strip()
                if "|" in data:
                    user, passw = data.split("|")
                    print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("password.txt not found.")

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
