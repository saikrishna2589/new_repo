# Write a script that generates the following GUI.

import PySimpleGUI as sg

text1 = sg.Text("Enter feet: ")
text2 = sg.Text("Enter inches: ")
Button = sg.Button("Convert")
input_box1 = sg.InputText()
input_box2 = sg.InputText()
window_title = " onverter"

create_GUI = sg.Window(window_title, layout=[[text1, input_box1], [text2, input_box2], [Button]])

create_GUI.read()
create_GUI.close()
