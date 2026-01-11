password = input("Enter a password: ")
has_digit = any (c.isdigit() for c in password)
if has_digit:
    print("Password contains at least one number")
else:
    print("Password does not contain any numbers")
