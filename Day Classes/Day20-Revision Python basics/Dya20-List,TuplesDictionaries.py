# Methods
# unlike functions ,methods are assosiated with certain type(Data)

"hello world".upper()
# o/p-->HELLO WORLD

"hello world".capitalize()
# o/p-->Hello world


"hello world".title()
# o/p-->Hello World

greeting = "hello world"
greeting.capitalize()
# o/p-->Hello world


# Methods that return an output
# below returns a new string but does not modify the original
greetings.title()
# o/p--Hello World

# List methods modify the original list

groceries = ['aloo', 'grapes', 'eggplant']
groceries.append['apples']

variable = groceries.append("apples")
# variable will be empty as no value will be returned using append method
# append method modifies its obejct
# so a method modifies its object when object is mutable
# all lists are mutable but strings are not mutable


groceries.sort()
# groceries.sort() will not give output unless we call groceries again as it
# modifies the object itself. this is different to greeting.title(),which gives
# o/p straight away but doesnt modify the original object itself
# this is because the object type 'greeting' is a string,which is immutable
# whilst groceries object type is list which is mutable


# so Strings are immutable . Lists are mutable


# a list of method for an object type. you enter
dir(str)
dir("hello")  # or instance of a string

dir(list)  # list object type
dir(float)
dir(int)

# How to create new methods?
# since methods are connected to their object types, we need to learn how
# to create a class or object type. ex-how to create string blue print


# ex- if i create booking system for airplane tickets, tickets itself can be a class
# each ticket would be an instance of the object class ticket
# ticket. cancel() can be a method created to cancel the exisitng booking
# ticket.delete() deletes user details from databse etc. so all these can be created


# List and Tuples

groceries = ["a", "b"]  # mutable

groceries1 = ("grayscale", 1920, "JPG")  # immutable

# for homogenours item types, we prefer using list
# and if new items can be added to list etc

# for Tuples, it is more meant to store heterogenous type


# Indexing
string = "vinegar"
groceries = ["vinegar", "olives", "beard"]

# Dictionary can be inside other data types as well such as lists
# List of dictionaries
persons_info = [{"first_name": "Sai", "last_name": "Krishna", "age": 34},
                {"first_name": "Nitya", "last_name": "Kanjarla", "age": 31}
                ]

# another form each key has multiple values put in a list
persons2 = {
    "first name": ["Sai", "Nitya"],
    "last name": ["Krishna", "Kanjarla"]
}

#to access dictionary values
persons2["first name"][1]
# o/p will be  "Nitya". here we are accessing dict datatype with first_name key and 2nd element within that key


persons_info[1]["first_name"]
#o/p will be 'Nitya as we are accessing 2nd element of a list with key 'first name' (as the data type is list of dict)

persons_