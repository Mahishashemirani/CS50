from validator_collection import checkers

email = input("enter your email: ")

if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")
