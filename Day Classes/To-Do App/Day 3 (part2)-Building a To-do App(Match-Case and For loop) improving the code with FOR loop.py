# what if we don't want to show the user the appended list by default?
# what if we only show it when user wants to see it in the output.
# For this we use "Match-Case" statement


# # The below block of code shows the appended list. Remove the # symbol from start to end of bookmark contained code
# to run if needed.

# user_prompt="Enter a to-do"

# todos=[]
# while True:
# user_to_do_list_entry_box = input(user_prompt)
# todos.append(user_to_do_list_entry_box)
# print(todos)##

# First , we need to ask the user - Do you want to add to the to-do list or see the existing to-do list?
user_prompt1 = "Pick: add (or) show (or) exit: "
Todo_list = []

while True:
    user_action_entry = input(user_prompt1)  # ask user whether to add to list or show  existing list
    user_action_entry = user_action_entry.strip()
    # stripping any spaces input by the user and then passing the stripped input to match-case
    # for relevant actions as required that need to be performed.

    match user_action_entry:  # Match case statement is a block just like WHILE True loop.

        case "add":
            enter_new_to_do_task = input("enter the to-do task you want to add to the list: ")
            Todo_list.append(enter_new_to_do_task)
            print(Todo_list)

        # improving the program with a 'For' loop The above code when we press show gives a list object. but end user
        # mostly wouldn't want to see '[' ']' and ',' that come with list object output in this case with typing show.
        # So we want to have one to-do item in one-line to keep the output clean

        # changing the show output as a result.
        case "show":
            for item in Todo_list:
                print(item)

        # what is we want to add /show or exit? so we add another case-exit
        case "exit":
            break  # breaks the while loop

print("Good-bye for now.Have a nice day.Make sure to smile,keep calm and focus")
