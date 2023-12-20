
# task print hello 9 times

x = 1
while x < 10:
    x = x + 1
    print('Hello')

# task create a list of to-do tasks for 6 entries
user_prompt = "Enter your to-do task:"
i = 0
to_do_list = []

while i < 6:
    # you can store 6 to-do tasks in your list with below while loop
    i = i + 1
    user_entry = input(user_prompt)
    user_entry = user_entry.title()
    to_do_list.append(user_entry)
    print(to_do_list)