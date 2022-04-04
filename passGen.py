import string
import random
import sys
import pm_rw
import bcolor
import os
import auth
from cryptography.fernet import Fernet


characters = list(string.ascii_letters + string.digits + "!@#$%^*()")


def main():
    os.system('cls')
    where = sys.argv[1]
    length = int(sys.argv[2])

    random.shuffle(characters)

    password = []
    for _ in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)


    key = pm_rw.load_key()
    fernet = Fernet(key)

    encrypted = pm_rw.read_file()
    decrypted = fernet.decrypt(encrypted)
    pm_rw.write_file(decrypted)

    with open("data.txt", "rb") as file:
        output = file.read()
    
    message_dict = eval(output)
    message_dict[where] = password
    message = str(message_dict).encode()
    print(f"Generated password for {where}:\n{password}")

    with open("data.txt", "wb") as file:
        file.write(message)

    changed = pm_rw.read_file()
    encrypted = fernet.encrypt(changed)
    pm_rw.write_file(encrypted)


if __name__ == "__main__":
    if auth.authentication():
        main()
        input(bcolor.bcolors.BOLD+"Press Enter to clear screen..."+bcolor.bcolors.ENDC)
        os.system('cls')
    else:
        os.system('cls')
        print(bcolor.bcolors.FAIL+"Incorrect Password!"+bcolor.bcolors.ENDC)