# Steps of building a program
# 1.Design the FrontEnd
# 2.Code the FrontEnd
# 3.Code the backend
# 4.Finish up

#Task --Extract zipfiles and unzip into a folder

import PySimpleGUI as sg
from BEday18ZipExtractorfunction import extract_archive

#step2--> code the Front End
sg.theme("LightBrown2")

label1=sg.Text("Select zip archive:")
input1=sg.Input()

# we choose FileBrowse type .If multiple files selection is needed, we need to select FilesBrowse as in case of
#selecting mutliple files for zipping the files.Here we select one zip file for unzipping
choose_button1=sg.FileBrowse("Choose", key="ziparchive")

label2=sg.Text("Select destination directory:")
input2=sg.Input()
choose_button2=sg.FolderBrowse("choose",key="folder_dir")

extract_button=sg.Button("Extract")

# we will show 'Extraction completed' after program is completed.so the label is empty.
# it gets updated based on the key call and .update method
output_label=sg.Text(key="output",text_color="green")

window= sg.Window("Archive Extractor",
                  layout=[[label1,input1,choose_button1],
                          [label2,input2,choose_button2],
                          [extract_button,output_label]])

while True:
    event,values=window.read()
    print(event,values)

    # storing the ziparchive path in zipfile_chosenpath variable and destination dir
    # in 'destination_chosen_path' variable. This will help us call the zip extractor function with these arguments
    zipfile_chosen_path=values["ziparchive"]
    destination_chosen_path=values["folder_dir"]
    extract_archive(zipfile_chosen_path,destination_chosen_path)
    window["output"].update(value="Extraction Completed",text_color="black")

window.close()


# Step 3--Code the backend. we will create a separate file for backend and call it using a function



