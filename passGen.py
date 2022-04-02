import string
import random
import sys
from cryptography.fernet import Fernet


characters = list(string.ascii_letters + string.digits + "!@#$%^*()")


def main():
    where = sys.argv[1]
    length = int(sys.argv[2])

    random.shuffle(characters)

    password = []
    for _ in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    message = f"&{where}: {password}"
    message = message.encode()

    print(f"Generated password for {where}:\n{password}")

    key = load_key()
    fernet = Fernet(key)

    encrypted = read_file()
    decrypted = fernet.decrypt(encrypted)
    write_file(decrypted)

    with open("data.txt", "ab") as file:
        file.write(message)

    changed = read_file()
    encrypted = fernet.encrypt(changed)
    write_file(encrypted)


def load_key():
    with open("C:/Users/Mikołaj/.en/filekey.key", "rb") as filekey:
        return filekey.read()


def read_file():
    with open("data.txt", "rb") as enc_file:
        return enc_file.read()


def write_file(decrypted):
    with open("data.txt", "wb") as dec_file:
        dec_file.write(decrypted)


if __name__ == "__main__":
    main()
