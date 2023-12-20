import re
user_entry_pass='Enter your Password: '
enter_password=input(user_entry_pass)
if len(enter_password) >=8 and re.search(r'\d+',enter_password) and re.search(r'[A-Z]',enter_password):
    print('Strong Password')
else:
    print('Weak password.Please consider changing it for security purposes')