from validator_collection import validators, checkers, errors
import sys

check_mail = input("Email à valider : ")

try:
    email_address = validators.email(check_mail)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    print("Please enter a value")
    sys.exit(0)
except errors.InvalidEmailError:
    print("Invalid")
    sys.exit(0)

print("Valid")