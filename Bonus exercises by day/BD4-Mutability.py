# Mutability
# suppose you have a folder with 3 tex files whose names are in the list below. you want to change '.' to '-'
# for ex- 3.Presentations.txt will need to be 3-Presentations.txt.

# so we are taking about doing something to each of the objects in the list repeatedly

filenames = ["1.Raw Data.ext", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-',1)
    print(filename)

# in business world, if you want to change name of the files rather than just printing each filename, you can use
# file.rename(filename)


# we can't use filename[1]="-" (check python console) as filename[1] is a '.' and it doesnt support item assignment.
# only int value can be assigned so filename[1] needs to be a int. strings dont support item assignment.
# Strings are immutable. They cannot be changed
# list are mutable. workaround to change string objects is to use .replace method
#'1' in the formula means only change the 1st occurance and ignore others


# A tuple is an immutable version of a list. so if you want list to not be mutated or changed, use a tuple

#Tuple is a list with '()' instead of '[]'

filename_tuple=("1.Raw Data.ext", "2.Reports.txt", "3.Presentations.txt")
type(filename_tuple)

# when you try to change an object within tuple using item assignment,you get TypeError: 'tuple' object does not support item assignment
#unlike List. (for ex- filename_tuple[1]='hey' will return an error. so only lists are mutable. Strings and Tuples are immutable
#string value can be amended using .replace method and assigning to new vatiable

#Likewise tuples dont have an append method as well since the original created tuple is immutable.
#append is hence method of a list.

