import PySimpleGUI as sg

import modules.Functions

text = sg.Text("Welcome")
button = sg.Button("Delete", key="delete")
window = sg.Window('My App', layout=[[text], [button]])


while True:
    event, values = window.read()
    print(window['delete'])

    # so 'choose' key has the values of the filepaths that were selected
    # the file paths are joined by ';' in the string ,so we use the split method
    # this will give us a list with separate file paths

