import validate_email

# Prompt user to input an email address
email = input("Enter an email address: ")

# Email validation
if validate_email.validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
