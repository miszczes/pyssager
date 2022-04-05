import string
import random
import sys
import os
import utils.pm_rw as pm_rw
import utils.bcolor as bcolor
import utils.auth as auth
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

    if is_File_Not_Empty("C:/Users/Mikołaj/Desktop/python/worktools/passManager/data.txt"):
        encrypted = pm_rw.read_file()
        decrypted = fernet.decrypt(encrypted)
        message_dict = eval(decrypted)
        message = add_dict(message_dict, where, password)
    else:
        message_dict = {}
        message = add_dict(message_dict, where, password)

    print(f"Generated password for {where}:\n{password}")

    encrypted = fernet.encrypt(message)
    pm_rw.write_file(encrypted)

def is_File_Not_Empty(fpath: str):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def add_dict(dict: dict, where: str, password: str):
    dict[where] = password
    return str(dict).encode()


if __name__ == "__main__":
    if auth.authentication():
        main()
        input(bcolor.bcolors.BOLD+"Press Enter to clear screen..."+bcolor.bcolors.ENDC)
        os.system('cls')
    else:
        os.system('cls')
        print(bcolor.bcolors.FAIL+"Incorrect Password!"+bcolor.bcolors.ENDC)