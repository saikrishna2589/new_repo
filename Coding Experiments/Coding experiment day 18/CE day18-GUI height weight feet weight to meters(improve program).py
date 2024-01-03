# convert feet and height into meters using GUI

import PySimpleGUI as sg

sg.theme("black")
textbox1 = sg.Text("Enter feet: ")
textbox2 = sg.Text("Enter inches: ")

inputbox1 = sg.InputText(key='feet')
inputbox2 = sg.InputText(key='inches')

button = sg.Button("Convert")
button_2 = sg.Button("Exit", key='Exit_button')

# creating empty text box to be updated at the end of the program when successfully run
convert_to_meters = sg.Text(key='value_in_meters')

gui = sg.Window("Converter", layout=[[textbox1, inputbox1], [textbox2, inputbox2], [button, convert_to_meters,button_2]])

while True:
    try:
        event, values = gui.read()
        match event:
            case "Convert":
                print(event, values)

                # printing feet and height
                print(values['feet'])
                print(values['inches'])

                metres = str(float(values['feet']) * 0.3048 + float(values['inches']) * 0.0254)
                gui['value_in_meters'].update(value=f"{metres} m", text_color='white')

                # if event ='Exit_button'

            case "Exit_button":
                break

            case sg.WIN_CLOSED:
                break

    except ValueError:
        sg.Popup("Please enter the two numbers in the input boxes")


gui.close()
# 2ft × 0.3048 + 3in × 0.0254
