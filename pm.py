import os
import utils.pm_rw as pm_rw
import utils.bcolor as bcolor
import utils.auth as auth
from cryptography.fernet import Fernet

def print_out(dct):
    print(bcolor.bcolors.HEADER+"PASSWORD LIST:"+bcolor.bcolors.ENDC)
    for what, pword in dct.items():
        print(f"{what}: {pword}")
    print()

def main():
    key = pm_rw.load_key()
    fernet = Fernet(key)

    enc_file = pm_rw.read_file()
    decrypted = (fernet.decrypt(enc_file)).decode()
    res = eval(decrypted)
    os.system('cls')
    print_out(res)
    return res

if __name__ == "__main__":
    if auth.authentication():
        main()
        input(bcolor.bcolors.BOLD+"Press Enter to clear screen..."+bcolor.bcolors.ENDC)
        os.system('cls')
    else:
        os.system('cls')
        print(bcolor.bcolors.FAIL+"Incorrect Password!"+bcolor.bcolors.ENDC)