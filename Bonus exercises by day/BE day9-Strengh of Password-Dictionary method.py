password = input("Enter your password: ")

results = {}  # changing the list to a dictionary so in the final output we can see which metric is satisfied or not (as
# key-value pari can help with that)

if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False

digit = False  # assigning initially digit=False
for p in password:
    if p.isdigit():
        digit = True

results["isdigit"] = digit

upper = False
for p in password:
    if p.isupper():
        upper = True

results["Uppercase"] = upper


print(results)

'''if  (results['length']==True and results['isdigit']==True  and results['Uppercase']==True):
    print('Strong Password')''' 'or alternative method below'

if all(results.values()):
    print("Strong Password")
else:
    print('Weak Password. Please change your Password')
