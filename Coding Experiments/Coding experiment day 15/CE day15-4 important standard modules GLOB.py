# 4 import modules CSV modules. glob module. webbrowser module, shutil module. they are likely to be used frequently

import glob

# glob function within glob module gives us 'list' of file paths that exist in the current directory with the specified
#name and extension.output is list containing the python file paths in the current directory with specified extension

myfiles= glob.glob("*.txt")
print(myfiles)

# suppose you want to print  all the text file paths in the
# 'glob function demo required files' folder .o/p will be a list of .txt extension file paths in the folder

mytextfiles=glob.glob('glob function demo required files/*.txt')
print(mytextfiles)


# reading contents from multiple text files in the 'glob function demo required files' folder
# this is possible by using glob first to store all filepaths with .txt extension in a list in the folder
#specified and then using for loop and with-open function to loop through each text file and read the contents
# and capitalise them
for filepath in mytextfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())