#opens the file in read mode
user_file = open("C:/Users/saikr/Downloads/members.txt", "r")
read_user_data = user_file.readlines()  #sam, john, daniel
user_file.close()


# asks user to enter the user. and the user gets appended.
user_new_data_input = input("Add a new member:")+"\n"
read_user_data.append(user_new_data_input)

#creating file again and overwriting the data
file_recreate= open("C:/Users/saikr/Downloads/members.txt","w")
data_load = file_recreate.writelines(read_user_data)
file_recreate.close()

#reading the updated data
user_file1 = open("C:/Users/saikr/Downloads/members.txt", "r")
read_user_data1 = user_file1.readlines()
print(read_user_data1)

# converts list to a string format

print("".join(read_user_data1))



#2nd method
#member = input("Add a new member: ")

#file = open("members.txt", 'r')  #open the file in read mode
#existing_members = file.readlines()  #read the data in the file object
#file.close()  #close the file

#existing_members.append(member + "\n")  #append to existing list based on user input

#file = open("members.txt", 'w')  #open file in write mode
#existing_members = file.writelines(existing_members)
#file.close()

