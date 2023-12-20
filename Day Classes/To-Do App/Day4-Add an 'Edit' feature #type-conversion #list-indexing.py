# Task 1- What if user does not enter 'add' , 'show' or 'exit' and enters something different. how to show
# message back to user perhaps saying 'input not valid.Please re-enter'


# we want to add a new feature for editing the to-do list. how do we go about adding the feature ?
user_prompt = " Type add (or) show (or) exit (or) modify: "
To_do_list = []

while True:
    user_display = input(user_prompt)
    user_display = user_display.strip()
    user_display = user_display.lower()

    match user_display:
        case "add":
            user_input_to_do_list = input("what item do you want to add to the to-do list? ")
            To_do_list.append(user_input_to_do_list)
            print(To_do_list)

        case "show" | "display":  # using Bitwise 'OR' operator
            for i in To_do_list:
                i = i.title()  # adding title case for each of the To-do items using the for loop before printing the
                # output.
                print(i)

        case "modify":
            for i in To_do_list:
                i = i.title()
                print(i)
            user_modify = int(input("what numbered task do you want to modify from the above?"))
            user_modify = user_modify - 1
            # above code, we are converting user input to int format as list index below accepts only numbers as input
            # to retrieve list indices
            to_do_list_task_to_amend = To_do_list[user_modify]
            print("the task you want to amend is :" + str(to_do_list_task_to_amend).title())
            new_user_to_do_entry = input("Enter the replacement for " + str(to_do_list_task_to_amend).title() + " :")
            To_do_list[user_modify]= new_user_to_do_entry
            print(To_do_list)

            # we will use 'list indexing' method to extract that numbered task from the array to-do list

        case "exit":
            break

        case random_entry:
            print("input not valid.Please re-enter from options provided")

        # the variable random_entry in this case does not need to be defined in the code.
        # it is defined on the fly with the entry of the user if it doesnt belong to 'add','show' or 'exit'

print("Goodbye for now!See you soon. Remember to SMILE AND Be Happy keep Happy")

# we want to add a new feature for editing the to-di list. how do we go about adding the feature
