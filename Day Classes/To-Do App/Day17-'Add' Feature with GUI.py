import PySimpleGUI as sg

import modules.Functions

# creating a text type .This creates a label on the Window
label = sg.Text("Type in a to-do")

# creating an inputtext instance
input_box = sg.InputText(tooltip="Enter todo", key='Todo')

add_button = sg.Button("Add")

# creating a 'Window' instance
# we are adding font ,which needs to be tuple . it has 2 arguments.

view_window = sg.Window('My To-Do App',
                        layout=[[label], [input_box, add_button]],
                        font=('Helvetica', 20))

# applying the read method to the window instance.
# This will make the window display graphically on the screen

# storing the read method output on the window type in a variable printing the variable will give tuple with the
# label of the button ('add') and dictionary with key and value of input box

# tuple will have 2 values .1st value will be the button label and 2nd dictionary with inputbox key-value

# we are placing the window read method variable in the while loop.
# this will help the program to keep adding the values without the window type getting closed as window.close method
# is outside the indent.

while True:
    event, values = view_window.read()
    print(event)
    print(values)

    # now we rae ready to add match case statement
    match event:
        case 'Add':
            todos = modules.Functions.get_todo_list()
            new_todo = values['Todo'] + "\n"
            todos.append(new_todo)
            modules.Functions.write_to_do_list(todos)

        # To avoid the error of 'KILL APPLICATION' when we press the close window of the GUI, we write another case
        # statement PySimpleGUI has WIN_CLOSED type which checks if program is open or not. when we close the GUI
        # using the 'red cross', we don't get an error anymore as we are using break statement which breaks the while
        # loop. so we don't get the 'KILL APPLICATION ' error anymore when closing the GUI

        case sg.WIN_CLOSED:
            break

view_window.close()
