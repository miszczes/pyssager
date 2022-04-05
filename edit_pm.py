import os
import pm
import utils.pm_rw as pm_rw
import utils.bcolor as bcolor
import utils.auth as auth
from cryptography.fernet import Fernet

def main():
    result_dict = pm.main()

    rm = input("What password would you like to remove? [type place]:")
    os.system('cls')

    remove_key = result_dict.pop(rm, None)

    if remove_key != None:
        print(bcolor.bcolors.OKGREEN+f"Password for {rm} has been removed!"+bcolor.bcolors.ENDC)
        print()
    else:
        print(f"No key has been removed for {rm}. \n"+bcolor.bcolors.FAIL+"The password doesn't exist!"+bcolor.bcolors.ENDC)
        print()
        exit()

    pm.print_out(result_dict)

    res = str(result_dict).encode()
    key = pm_rw.load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(res)
    pm_rw.write_file(encrypted)

if __name__ == "__main__":
    if auth.authentication():
        main()
        input(bcolor.bcolors.BOLD+"Press Enter to clear screen..."+bcolor.bcolors.ENDC)
        os.system('cls')
    else:
        os.system('cls')
        print(bcolor.bcolors.FAIL+"Incorrect Password!"+bcolor.bcolors.ENDC)
