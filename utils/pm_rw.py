import configparser

config = configparser.ConfigParser()
config.readfp(open(r"")) #config.ini filepath
authkey_path = config.get("file paths", "authkey_path")
authfile_path = config.get("file paths", "authfile_path")
filekey_path = config.get("file paths", "filekey_path")
passfile_path = config.get("file paths", "passfile_path")

def load_key():
    with open(filekey_path, "rb") as filekey:
        return filekey.read()


def read_file():
    with open(passfile_path, "rb") as enc_file:
        return enc_file.read()


def write_file(decrypted):
    with open(passfile_path, "wb") as dec_file:
        dec_file.write(decrypted)

def load_auth():
    with open(authkey_path, "rb") as authkey:
        return authkey.read()

def read_auth():
    with open(authfile_path, "rb") as enc_auth:
        return enc_auth.read()


def write_auth(decrypted):
    with open(authfile_path, "wb") as dec_auth:
        dec_auth.write(decrypted)