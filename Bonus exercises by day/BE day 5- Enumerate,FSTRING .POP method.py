

# print the o/p below from the list provided (in alphabetical order with index)
# 1.Ben
# 2.John
# 3.Sen

waiting_list = ["sen", "ben", "john"]
waiting_list.sort()  #this method modifies and sorts the list.

# for loop
# title
# enumerate

for index, w in enumerate(waiting_list):
    print(f"{index+1}.{w.title()}")  # you can also use .capitalize instead of .title()

