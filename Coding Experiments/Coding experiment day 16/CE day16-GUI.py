
import modules.Functions

#installed earlier the package and import the package PySimpleGUI.
#this contains the GUI
import PySimpleGUI as sg

# creating a text type .This creates a label on the Window
label= sg.Text("Type in a to-do")

# creating an inputtext instance
input_box=sg.InputText(tooltip= "Enter todo")

add_button=sg.Button("Add")

#creating a 'Window' instance
view_window= sg.Window('My To-Do App', layout=[[label],[input_box],[add_button]])

# applying the read method to the window instance.
#This will make the window display graphically on the screen
view_window.read()
view_window.close()

