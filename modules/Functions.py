
# variable constants are defined using CAPTITAL letters as standard practice.
#if file name changes, only this path can be changed and everything works
FILEPATH="C:/Users/saikr/Documents/pycharm projects/Day Classes/To-Do App/To_do_list.txt"

def get_todo_list(filepath=FILEPATH):
    """This function open the file in the filepath provided ,read all the lines and saves it as a list in a variable
        and returns the list as the output"""  # This is a docstring
    with open(filepath, 'r') as file:
        to_do_list_local = file.readlines()
    return to_do_list_local


# create function with 2 parameters: file location and list to be written to the file.
def write_to_do_list(to_do_list_local, filepath_local=FILEPATH):
    """ This function takes in the updated list as the first argument and default as the file name to be written to or
         created."""
    with open(filepath_local, 'w') as file2_local:
        file2_local.writelines(to_do_list_local)


'The below will run only on the main file,which is this file. but if we import this module to another file such as '
'"Day14-Organising the code-Import Modules.py",they wont be run. this can help it test cases if you want to test o/p'
'in the main file but dont want to show o/p in the file where the module is imported'

print(__name__) # this variable is a built in python function and gives the o/p as __main__,
# In the module where this script is being imported to, the value of the __name__ will be equal to the file name,
#' modules.Functions' in this case

if __name__ == "__main__":
    print("Hello")
    print(get_todo_list())
