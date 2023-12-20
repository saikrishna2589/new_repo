# Custom functions help in avoiding redundant code.for ex-Here we use 'with function to read files' in every if
# condition custom functions can help reduce that redundancy.
# Custom functions are defined on top of the code usually outside the loop.

# giving the default parameter for the file we are reading from for get_todo_list function as it is a default

"""we are commenting out the functions here as we will use modules to import them
from another file """
'''
def get_todo_list(filepath="To_do_list.txt"):
    """This function open the file in the filepath provided ,read all the lines and saves it as a list in a variable
        and returns the list as the output"""  # This is a docstring
    with open(filepath, 'r') as file:
        to_do_list_local = file.readlines()
    return to_do_list_local


# create function with 2 parameters: file location and list to be written to the file.
def write_to_do_list(to_do_list_local, filepath_local="To_do_list.txt"):
    """ This function takes in the updated list as the first argument and default as the file name to be written to or
         created."""
    with open(filepath_local, 'w') as file2_local:
        file2_local.writelines(to_do_list_local)

'''

'Here we are importing get_todo_list and write_to_do_list functions'
'from  external python file."Functions.py", saved in modules directory '
'This will help code to stay organised and not make it too long'


from modules.Functions import get_todo_list, write_to_do_list

'2nd method to import functions from another file'
'import Functions (this means you will need to mention'
' Functions.get_todo_list() instead of get_todo_list'

user_prompt = " Type add (or) show (or) exit (or) modify (or) complete : "
while True:
    user_display = input(user_prompt)
    user_display = user_display.strip()
    user_display = user_display.lower()

    if user_display.startswith("add"):
        'user_input_to_do_list = input("what item do you want to add to the to-do list? ") + "\n"'
        user_input_to_do_list = user_display[4:]

        '''file = open("To_do_list.txt", 'r')  # read the existing To_do_list items
        To_do_list = file.readlines()  # read the existing To_do_list items
        file.close()'''

        # instead of a 'with context manager to read the file, as it is repetitive across all if clauses,we use
        # custom function defined at the beginning of the code.
        To_do_list = get_todo_list()

        '''# Optimising the code using '#with instead of open function directly as above
        'with open("To_do_list.txt", 'r') as file:
            To_do_list = file.readlines()  # you 'don't need to close the file '''

        To_do_list.append(user_input_to_do_list + "\n")

        # how to store the to-do list in a file. In below, we use open() ,which is a file object and write
        # into the To_do_list.txt text file created in the same directory('w--> write.'r'-->read)
        write_to_do_list(To_do_list)

        # writelines is a method available for file objects.this writelines method
        # gets 'list' as an argument.Here we are giving our To_Do_List as an argument to the writelines method
        # file2.write() is used for text and same for file2.read()

    # we use enumerate function so we can index number along with the to-do list.
    # there is a space between the index number and the to-do list obejcts in the o/p. To reduce that, we
    # will need to use f-strings

    elif user_display.startswith("show") or user_display.startswith("display"):  # using Bitwise 'OR' operator

        To_do_list = get_todo_list()

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

    elif user_display.startswith("modify"):

        try:  # we are using try for error handling. if user enters text after 'modify' for instance,
            # program abruptly stops and gives error that user may not understand. so we simplify and customise
            # the error through 'try except' error handling

            To_do_list = get_todo_list()

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

                # using function for writing the file (2 parameters- what file and what to write in the file)
            write_to_do_list(To_do_list)

            new_todo = [item.strip("\n") for item in To_do_list]  # this is a list comprehension method
            print(new_todo)

        except ValueError:
            print("Your input is not valid.")
            continue  # continue command will ignore anything coming after this statement and goes back to execute code
            # from beginning

    # we will use 'list indexing' method to extract that numbered task from the array to-do list.
    # Adding another case statement to help user mark the to-do as complete. adn if complete, item will be
    # removed from to-do list This will be manipulation as in we are manipulating the list. If complete,
    # we want it removed from the list. so in such cases for manipulation of the list or any of the objects,
    # we need to think about 'METHODS'

    elif user_display.startswith("complete"):
        try:

            # using pre-defined functions to read the file and save the list to the To_do_list variable
            To_do_list = get_todo_list()

            for index, i in enumerate(To_do_list):
                todo_tasks = f"{index + 1}.{i}"
                print(todo_tasks)

            task_completed = user_display[9:]
            task_completed = int(task_completed) - 1
            item_to_be_removed = To_do_list[task_completed].strip('\n')
            To_do_list.pop(task_completed)  # delete the completed task index

            # printing the item that is completed
            message = f"To-do item'{item_to_be_removed}'removed from the list"
            print(message)

            # printing all remaining items on to-do list
            print("remaining items on to do list: ")

            # display the remaining tasks one line each in custom format
            for index, i in enumerate(To_do_list):
                remaining_todo_tasks = f"{index + 1}.{i}"
                print(remaining_todo_tasks)

            # write updated list back to the file
            write_to_do_list(To_do_list)

        except IndexError:
            print("Your input is invalid.Index out of range")
            continue

    elif user_display.startswith("exit"):
        break

    else:
        print("Command is not valid.Make sure you start with add/show/modify/complete")

# the variable random_entry in this case does not need to be defined in the code.
# it is defined on the fly with the entry of the user if it doesn't belong to 'add','show' or 'exit'

print("Goodbye for now!See you soon. Remember to SMILE AND Be Happy keep Happy")

print(help(get_todo_list))
print(help(write_to_do_list))
