# While loops

#while True:
    #password = input("Enter password: ")

"""password = input("Enter password: ")

while password != "pass1":
    password = input("Enter password: ")

print("Password is correct")
"""



"""
#For-Loops #runs through as many times as part of the data type in this case list

usernames=["John","Sim","spongy"]

for username in usernames:
    username.capitalize()
    print()

"""


#Match-Case- if value is same as other value
"""
username=input("Enter username: ")

match username:
    case "sai":
        print("Welcome"+ " " + "sai")

    case "sim":
        print("Welcome" + " " + "sim")

    case _:
        print("invalid username")
"""


#If-Elif-Else -->For more complex comparisons than match-case


"""
password="pass"
if len(password)>=5:
    print("password is strong")
elif len(password)==4:
    print("password is ok")
else:
    print("Password is weak")

"""


#f-Strings

"""
first_name="naya"
last_name="anand"

message=f"Hello {first_name.capitalize()},how are you? is your last name {last_name.capitalize()}? "

print(message)

"""


