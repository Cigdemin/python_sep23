password = False
while password == False :
    psswrd = input('''Please provide a password meets with following requirements:  
** The password must be at least 8 characters long.
** The password must contain at least one uppercase letter.
** The password must contain at least one lowercase letter.
** The password must contain at least one digit.
** The password must contain at least one special character (e.g., @, #, $, etc.).''')
    #1 check password length it must be 8 character
    #2 check pasword muct contain one uppercase and one lowercase and one number/digit and one special character
    char_list=("[@_!#$%^&*()<>?/\|}{~:]")
    is_upper = any(x.isupper() for x in psswrd)
    is_lower = any(x.islower() for x in psswrd)
    is_digit = any(x.isdigit() for x in psswrd)
    for x in psswrd:
        if x in char_list:
            is_spec_char = True
            break

    if len(psswrd) == 8 and is_upper and is_lower and is_digit and is_spec_char :
        password = True
        print(f"Your password is: {password}")
    else:
        password = False
        print("Please enter a valid password")

