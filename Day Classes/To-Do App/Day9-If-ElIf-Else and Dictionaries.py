# Task 1- What if user does not enter 'add' , 'show' or 'exit' and enters something different. how to show
# message back to user perhaps saying 'input not valid.Please re-enter'


# we want to add a new feature for editing the to-do list. how do we go about adding the feature ?


# Day5- When user wants to modify a task in the list, he/she currently has to count the number in the list that they
# want to modify manually. we want to make user experience better by adding number in front of the printed modify
# output. how to achieve this? Answer-Enumerate() function

user_prompt = " Type add (or) show (or) exit (or) modify (or) complete : "

while True:
    user_display = input(user_prompt)
    user_display = user_display.strip()
    user_display = user_display.lower()

    if "add" in user_display:
        'user_input_to_do_list = input("what item do you want to add to the to-do list? ") + "\n"'
        user_input_to_do_list = user_display[4:]

        '''file = open("To_do_list.txt", 'r')  # read the existing To_do_list items
        To_do_list = file.readiness()  # read the existing To_do_list items
        file.close()'''

        # Optimising the code using '#with instead of open function directly as above
        with open("To_do_list.txt", 'r') as file:
            To_do_list = file.readlines()  # you 'don't need to close the file in t

        To_do_list.append(user_input_to_do_list+"\n")

        # how to store the to-do list in a file. In below, we use open() ,which is a file object and write
        # into the To_do_list.txt text file created in the same directory('w--> write.'r'-->read)
        with open('To_do_list.txt', 'w') as file2:
            file2.writelines(To_do_list)

        # writelines is a method available for file objects.this writelines method
        # gets 'list' as an argument.Here we are giving our To_Do_List as an argument to the writelines method
        # file2.write() is used for text and same for file2.read()

    # we use enumerate function so we can index number along with the to-do list.
    # there is a space between the index number and the to-do list obejcts in the o/p. To reduce that, we
    # will need to use f-strings

    elif "show" in user_display or "display" in user_display:  # using Bitwise 'OR' operator

        with open('To_do_list.txt', 'r') as read_todo_list:
            To_do_list = read_todo_list.readlines()

        '''new_todo = []  # creating an empty list so we can place the  items in the list after removing the "\n" as
        # per below . we using for loop to iterate through the to-do list and remove the "\n"'''

        '''for item in To_do_list:
            new_item = item.strip("\n")
            new_todo.append(new_item)'''

        # Another method to remove the "\n" or modify items in a list is -List comprehension
        # it is a shorter syntax than for-loop. it takes a single line and starts with "[]" and
        # we write in line composition for loop(that is for loop in one line)

        new_todo = [item.strip("\n") for item in To_do_list]  # this is a list comprehension method
        print(new_todo)

        for index, i in enumerate(new_todo):
            i = i.title()  # adding title case for each of the To-do items using the for loop before printing the
            output1 = f"{index + 1}.{i}"
            print(output1)
        print(f"Length of the list is: {index + 1}")  # last value of the index is stored in the index value
        # outside the for loop
        # but actual proper way to get length of a list is to use length function
        print(f"Length of the list is :{len(new_todo)}")

    elif "modify" in user_display:

        with open('To_do_list.txt', 'r') as read_todo_list:
            To_do_list = read_todo_list.readlines()

        for index, i in enumerate(To_do_list):
            i = i.title()
            output = f"{index + 1}.{i}"
            print(output)
            # the print function prints the o/p but there are spaces between index and item object in the print.

            # what if you don't want spaces in the o/p between index and item object. Enter 'Fstring'
        '''user_modify = int(input("what numbered task do you want to modify from the above?"))'''
        user_modify = user_display[7:]
        user_modify = int(user_modify) - 1
        # above code, we are converting user input to int format as list index below accepts only numbers as input
        # to retrieve list indices

        to_do_list_task_to_amend = To_do_list[user_modify]
        print("the task you want to amend is :" + str(to_do_list_task_to_amend).title())

        new_user_to_do_entry = input("Enter the replacement for " + str(to_do_list_task_to_amend).title() + " :")
        To_do_list[user_modify] = new_user_to_do_entry + "\n"

        for index, i in enumerate(To_do_list):
            i = i.title()  # adding title case for each of the To-do items using the for loop before printing the
            # output.
            output2 = f"{index + 1}.{i}"
            print(output2)

        with open('To_do_list.txt', 'w') as file3:
            file3.writelines(To_do_list)

        new_todo = [item.strip("\n") for item in To_do_list]  # this is a list comprehension method
        print(new_todo)

    # we will use 'list indexing' method to extract that numbered task from the array to-do list

    # Adding another case statement to help user mark the to-do as complete. adn if complete, item will be
    # removed from to-do list This will be manipulation as in we are manipulating the list. If complete,
    # we want it removed from the list. so in such cases for manipulation of the list or any of the objects,
    # we need to think about 'METHODS'

    elif "complete" in user_display:

        with open("To_do_list.txt", "r") as file_complete:
            file_all = file_complete.readlines()

        for index, i in enumerate(file_all):
            todo_tasks = f"{index + 1}.{i}"
            print(todo_tasks)

        task_completed = user_display[9:]
        task_completed = int(task_completed) - 1
        item_to_be_removed = file_all[task_completed].strip('\n')
        file_all.pop(task_completed)  # delete the completed task index

        # printing the item that is completed
        message = f"To-do item'{item_to_be_removed}'removed from the list"
        print(message)

        # printing all remaining items on to-do list
        print("remaining items on to do list: ")

        # display the remaining tasks one line each in custom format
        for index, i in enumerate(file_all):
            remaining_todo_tasks = f"{index + 1}.{i}"
            print(remaining_todo_tasks)

        # write updated list back to the file
        with open("To_do_list.txt", "w") as file_complete1:
            file_complete1.writelines(file_all)

    elif "exit" in user_display:
        break

    else:
        print("Command is not valid.Make sure you start with add/show/modify/complete")

# the variable random_entry in this case does not need to be defined in the code.
# it is defined on the fly with the entry of the user if it doesn't belong to 'add','show' or 'exit'

print("Goodbye for now!See you soon. Remember to SMILE AND Be Happy keep Happy")
