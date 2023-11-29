# Create a Python function named validate_email that takes an email address as input and checks if it is valid based on the following criteria:
# 1. The email address should contain a single “@” symbol.
# 2. The local part (before the “@”) should not start or end with a period (“.”) and should not have consecutive periods.
# 3. The domain part (after the “@”) should contain at least one period and should not start or end with a period.
# 4. The function should return a boolean value, where True indicates that the email is valid, and False indicates that it is not.
# Input:
# email_validity = validate_email("user@example.com")
# print(email_validity)
# Output:
# True
def validate_email(mail):
    if "@" in mail and "." in mail:
        if mail.find("@") > mail.find("."):
            return True
            print(mail.find("@"))
        else:
            return False
    else:
        print("you are doing sth wrong")

validate_email("cigmenci@hotmail.com")