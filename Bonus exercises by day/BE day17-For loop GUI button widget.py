
# build an app with difference buttons and keep it flexible as buttons can be added ,amended.

import PySimpleGUI as sg

buttons=['Add','Edit','Delete']
empty_button=[]


# here we are appending the list empty_button using a for loop and adding each button as a list.
#so list of lists format is passed on to the layout in sg.window

for button in buttons:
    empty_button.append([sg.Button(button)])

buttons_widget_app=sg.Window("Select",layout=empty_button)

buttons_widget_app.read()
buttons_widget_app.close()