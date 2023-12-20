

# task-ask user to enter a password and if correct stop the loop. if not correct keep prompting to enter the password

user_display = "Enter your password: "
password = "Thisisit"
incorrect_passwords = []
user_entered_password = input(user_display)

while user_entered_password != password:
    print("Please re-enter your password as the entered password is incorrect")
    user_entered_password = input(user_display)
    if user_entered_password == password:
        print("your password is correct. door unlocked. mission successful. go on to the next stage")

