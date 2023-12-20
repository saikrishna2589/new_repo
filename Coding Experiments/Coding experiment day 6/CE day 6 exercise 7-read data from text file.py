
#opening the file using open() function
file_a= open("C:/Users/saikr/Downloads/a.txt","r")
file_b= open("C:/Users/saikr/Downloads/b.txt","r")
file_c= open("C:/Users/saikr/Downloads/b.txt","r")


#reading the contents of the file using .read()method
read_file_a= file_a.read()
read_file_b= file_b.read()
read_file_c= file_c.read()


#printing the data into the console
print(read_file_a)
print(read_file_b)
print(read_file_c)


#more efficient solution
#filenames = ['a.txt', 'b.txt', 'c.txt']

#for filename in filenames:
    #file = open(filename, 'r')
    #content = file.read()
    #print(content)