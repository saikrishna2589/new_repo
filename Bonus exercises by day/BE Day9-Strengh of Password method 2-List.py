password = input("Enter your password: ")

results = []

if len(password) >= 8:
    results.append(True)
else:
    results.append(False)

digit = False  # assigning initially digit=False
for p in password:
    if p.isdigit():
        digit = True

results.append(digit)

upper = False
for p in password:
    if p.isupper():
        upper = True

results.append(upper)
print(results)
print(all(results))
# all is a function that takes input in a list form and returns True when all the items in the list are true. else it
# gives False

if all(results):
    print('Strong Password')
else:
    print('Weak Password. Please change your Password')



