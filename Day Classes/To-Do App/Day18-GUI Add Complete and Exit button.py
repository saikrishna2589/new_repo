import PySimpleGUI as sg

import modules.Functions

import time
# creating an empty text instance first and later we will populate with current time based on when program was run.

#GUI Theme
sg.theme("DarkGreen")
clock = sg.Text('',key='clock')

# creating a text type .This creates a label on the Window
label = sg.Text("Type in a to-do")

# creating an inputtext instance
input_box = sg.InputText(tooltip="Enter todo", key='Todo')

add_button = sg.Button("Add")

# we want to edit the layout to firstly show list of all to-dos and then give user option to 'edit' the to-do from tje
# List of to-dos

#size [45,10] is the size of 2 elements of the lsitbox.w=characters-wide, h=rows-high.i.ewidth of list box=45
# # characters and 10 rows high in the list box.i.e it displays 10 elements of to-do before scrolling
list_box = sg.Listbox(values=modules.Functions.get_todo_list(),
                      key='todos_existing',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

# creating a 'Window' instance
# we are adding font ,which needs to be tuple . it has 2 arguments.


view_window = sg.Window('My To-Do App',
                        layout=[[clock],
                                [label],
                                [input_box, add_button],
                                [list_box, edit_button, complete_button],
                                [exit_button]],
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

    #timeout=10 argument inside read method on windows gui helps to make the clock label available on GUI before anything is run
    #else clock is visible only after a selection is made
    #also timeout=10 would make the loop run every 200 milliseconds
    #this continuos running of the loop will help to see the time every second in the display
    event, values = view_window.read(timeout=200)

    #calling the strftime method to update the window['clock] label empty string with the time program was run
    view_window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # now we rae ready to add match case statement
    match event:
        case 'Add':
            todos = modules.Functions.get_todo_list()
            new_todo = values['Todo'] + "\n"
            todos.append(new_todo)
            modules.Functions.write_to_do_list(todos)

            # now to show the list box update real time after editing the values,
            # we are calling the list box key 'todos_existing' on the window instance and
            # using the .update method of the list box to update with new todos

            view_window['todos_existing'].update(values=todos)

        # we are adding 'Edit' button and then extracting the value of the dictionary key 'todos_existing'.this is a
        # list. if we want the values, we need to give the index [0] which is the first item of the list whatever
        # value user selects in the list of to-dos is what is captured as the value in the dictionary key

        case "Edit":

            try:
                todo_edit = values['todos_existing'][0]

                # the value that is entered in the input box is what will be edited to and is saved in to-do key ,
                # part of inputtext
                new_todo = values['Todo'] + "\n"
                todos = modules.Functions.get_todo_list()

                # we want to replace the value that would be editted would the new value
                # for this, we first check the index of the item in the list to be editted and store
                # in the 'index' variable
                index = todos.index(todo_edit)

                # we then replace that index with new_todo that user enters
                todos[index] = new_todo
                modules.Functions.write_to_do_list(todos)

                # now to show the list box update real time after editing the values,
                # we are calling the list box key 'todos_existing' on the window instance and
                # using the .update method of the list box to update with new todos

                view_window['todos_existing'].update(values=todos)

            except IndexError:

                # if user doesn't select any item and clicks 'Edit',we get IndexError. To avoid that, we are using
                # Try Except and in except part of the block, we define what to display to user instead of error. we
                # are here using a sg.popup method to popup window to user as command line messages cant be seen by
                # user.
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        # whenever we select an item in the list box of GUI, we want to dsplay in the
        # input text box . To do this, we use the event value 'todos_existing'

        case "Complete":
            try:
                # extracting the string out of the list in the values['todos_existing] key
                todo_to_complete = values['todos_existing'][0]

                # gets current list of to-dos
                todos = modules.Functions.get_todo_list()

                # we use remove method ,which is a part of a list method
                todos.remove(todo_to_complete)

                modules.Functions.write_to_do_list(todos)

                # updating the list box,which has a key 'todos_existing'
                # dynamically once completed item is removed
                view_window['todos_existing'].update(values=todos)

                # updating the input box to get rid of the item from the inputbox display as well.
                # input box has valur argument whilst listbox has 'values' argument
                view_window['Todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case 'Exit':
            break

        case 'todos_existing':

            # we are updating the current selection of user selection using values dictionary key 'todos_existing'and
            # extracting the string using [0] index and updating the input text box value with the user selection

            view_window['Todo'].update(value=values['todos_existing'][0])

        # To avoid the error of 'KILL APPLICATION' when we press the close window of the GUI, we write another case
        # statement PySimpleGUI has WIN_CLOSED type which checks if program is open or not. when we close the GUI
        # using the 'red cross', we don't get an error anymore as we are using break statement which breaks the while
        # loop. so we don't get the 'KILL APPLICATION ' error anymore when closing the GUI

        case sg.WIN_CLOSED:
            break

view_window.close()
