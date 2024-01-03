

#convert feet and height into meters using GUI

import PySimpleGUI as sg

textbox1 = sg.Text("Enter feet: ")
textbox2 = sg.Text("Enter inches: ")

inputbox1 = sg.InputText(key='feet')
inputbox2 = sg.InputText(key='inches')

button = sg.Button("Convert")

#creating empty text box to be updated at the end of the program when successfully run
convert_to_meters = sg.Text(key='value_in_meters')

gui = sg.Window("Converter", layout=[[textbox1, inputbox1], [textbox2, inputbox2], [button, convert_to_meters]])

while True:
    event, values = gui.read()

    # printing feet and height
    print(values['feet'])
    print(values['inches'])

    metres = str(float(values['feet']) * 0.3048 + float(values['inches']) * 0.0254)

    gui['value_in_meters'].update(value=f"{metres} m",text_color='white')

gui.close()
# 2ft × 0.3048 + 3in × 0.0254
