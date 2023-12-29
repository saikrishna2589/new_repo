import PySimpleGUI as sg


def km_to_miles(km):
    return km / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            # km is the number entered in the input text box.it has key 'kms' and is in the values dictionary. we
            # need to convert values['kms'] to float as it is of string type and cant be divided in the function
            # defined.

            km = float(values["kms"])
            # this km is divided by 1.6 in the function km_to_miles where km is the input argument to the function.

            # this function value that is converted to miles and stored in result
            result = km_to_miles(km)


            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()
