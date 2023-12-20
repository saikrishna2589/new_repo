# List Indexing Experiment 3

my_list = ['a', 'b', 'c']
z = my_list[2]

print(z)

# how do we get index values for the list above?

print(my_list.index('a'))  # index method . provide object to know the index of

dir(list)  # this lists all the method we can use for a list
dir(str)  # this shows all methods we can use against a string object

my_list.__setitem__('a', 'abc')  # this methods starting with '__' are internal python methods.
# we dont need to use them but we can.  the above method replaces the list object
# 'a' with 'abc'

# This is equivalent of saying

my_list[0] = 'abc'

#The background calls the internal method when we use this inthe front end.# so every change is being done by
#internal method. Python developers provided simple syntax for us


my_list.__getitem__(2)  # Output will be 'c' object in the list
#so my.list[2]  is equivalent to my_list__get_item__(2)