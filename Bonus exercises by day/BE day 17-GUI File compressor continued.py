import PySimpleGUI as sg
from BEday17Zipcreatorfunction import make_archive

text1 = sg.Text('Select files to compress')
text2 = sg.Text('Select destination folder')

input_box1 = sg.InputText(key='inputbox1')
input_box2 = sg.InputText(key='inputbox2')

# sg.FilesBrowse is programmed to help choose the files.
# sg.FolderBrowse is programmed to help select destination folder
# sg.Button will only add button with the chosen label
choose_button1 = sg.FilesBrowse("Choose", key='Files')
choose_button2 = sg.FolderBrowse("Choose", key='Folder')

compress_button = sg.Button('Compress')

#placing empty text label for now. once o/p or zip is successful, this will be overwritten
#and delivers a success message after compression
output_label= sg.Text( key="output",text_color='black',size=20)

creating_gui_window = sg.Window("File Zipper",
                                layout=[[text1, input_box1, choose_button1]
                                    , [text2, input_box2, choose_button2],
                                        [compress_button, output_label]])
while True:
    event, values = creating_gui_window.read()
    print(event, values)

    # so 'choose' key has the values of the filepaths that were selected
    # the file paths are joined by ';' in the string ,so we use the split method
    # this will give us a list with separate file paths

    file_paths = values["Files"].split(';')
    folder_path = values["Folder"]

    make_archive(file_paths, folder_path)
    creating_gui_window["output"].update(value="Compression completed!")

creating_gui_window.close()
