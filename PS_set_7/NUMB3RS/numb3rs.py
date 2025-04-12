import re
import sys


def main():
    if validate(input("IPv4 Address: ")) == True:
        print("Valide")
    else:
        print("Invalide")


def validate(ip):
    pattern = r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$"
    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
