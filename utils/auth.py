import os
import getpass
import utils.pm_rw as pm_rw
from sympy import false, true
from cryptography.fernet import Fernet

def authentication():
    key = pm_rw.load_auth()
    fernet = Fernet(key)

    auth_key = pm_rw.read_auth()
    decrypted = fernet.decrypt(auth_key)

    os.system("cls")
    pword = getpass.getpass()

    if pword.encode() == decrypted:
        return true
    else:
        return false


