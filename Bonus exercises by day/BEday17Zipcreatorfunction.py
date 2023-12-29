import zipfile
# we can use shutil module as well but it is not as powerful as zipfile module

import pathlib
# we are using pathlib.Path function to create a folder path that needs to be passed
#on to the Zipfile argument . Pathlib.Path creates folder path for us based on
#argument we provide. it is cleaner way to create paths

# we write  function and use ZipFile type within zipfile library to create
#zipfile object. to write we use 'w' mode. to extract , we need to use 'r' read mode
def make_archive (filepaths , destination_dir):
     dest_path= pathlib.Path(destination_dir,"compressed.zip")

     #zipfile type creates zipfile type object.this expected dest_dir and mode as input
     with zipfile.ZipFile(dest_path,'w') as file:
         for filepath in filepaths:

             # we are overwriting filepath as a complete filepath and then using arcname , we extract only name
             #of the file.this will not create multiple subfolders within the zip file to access the files.
             filepath=pathlib.Path(filepath)
             # the file zip object below has a write method
             file.write(filepath,arcname=filepath.name)


# the below says that if the function above is executed as the main script,
#then we call the function. this is used for testing purposes

if __name__=="__main__":
    make_archive(filepaths=["BE day16-GUI.py","BE day15- Build quiz app JSON.py",
                            "BE day 13-Calculating age.py"],destination_dir='destination day17 bonus zip creator')
