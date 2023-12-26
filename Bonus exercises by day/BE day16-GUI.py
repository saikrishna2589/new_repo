import PySimpleGUI as sg
text1= sg.Text('Select files to compress')
text2= sg.Text('Select destination folder')

input_box1=sg.InputText()
input_box2=sg.InputText()

#sg.FilesBrowse is programmed to help choose the files.
# sg.FolderBrowse is programmed to help select destination folder
#sg.Button will only add button with the chosen label
choose_button1=sg.FilesBrowse("Choose")
choose_button2=sg.FolderBrowse("Choose")

compress_button=sg.Button('Compress')

creating_gui_window= sg.Window("File Zipper",
                               layout=[[text1,input_box1,choose_button1]
                                      ,[text2,input_box2,choose_button2],
                                       [compress_button]])

creating_gui_window.read()
creating_gui_window.close()