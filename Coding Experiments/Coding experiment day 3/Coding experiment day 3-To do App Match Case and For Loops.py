# Task 1- What if user does not enter 'add' , 'show' or 'exit' and enters something different. how to show
# message back to user perhaps saying 'input not valid.Please re-enter'

user_prompt = "add (or) show (or) exit: "
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

        case "exit":
            break

        case random_entry:
            print("input not valid.Please re-enter from options provided")

        # the variable random_entry in this case does not need to be defined in the code.
        # it is defined on the fly with the entry of the user if it doesnt belong to 'add','show' or 'exit'

print("Goodbye for now!See you soon. Remember to SMILE AND Be Happy keep Happy")
