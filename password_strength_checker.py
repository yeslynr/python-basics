import string

password = input("Enter a password: ")

length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)

score = sum([length, has_upper, has_lower, has_digit, has_symbol])

if score <= 2:
    print("Password strength: WEAK")
elif score == 3 or score == 4:
    print("Password strength: MEDIUM")
else:
    print("Password strength: STRONG")
