user_entry_text = "Enter your Password: "
password = input(user_entry_text)

# function to check if password is weak or strong based on conditions

def strength(password):
    length_password = len(password)
    pass_length_check = False

    # checking password length condition
    if length_password >= 8:
        pass_length_check = True

        # checking upper case condition
    upper = False
    for p in password:
        if p.isupper():
            upper = True

    digit = False
    for d in password:
        if d.isupper():
            digit = True

    pass_check_list = [pass_length_check, upper, digit]
    result = all(pass_check_list)

    if result:
        r = "Strong password"
    else:
       r= "Weak Password"

    return r


password_strength_checker = strength(password)
print(password_strength_checker)
