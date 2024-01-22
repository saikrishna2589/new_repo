
#Creating files

with open("book.txt","w") as file:
    file.write("Hello there!")


content="""fdsfdsfjnsdfsdfjsdknfjsdnfsdf
sdsadasddsads
sadasdsa
asdasddas"""

#writing string that spans multiple lines into the file
with open("book.txt","w") as file:
    file.write(content)

with open("weather.txt","w") as file:
    file.writelines(["clouds\n","Sun\n", "sun\n"])


#Reading files
with open("book.txt",'r') as file:
    content= file.read()

with open("book.txt",'r') as file:
    content= file.readlines()
#readlines vs read method:readlines is for multiple lines so it reads everyline differently.use breaklines
#similar to writelines for writing multiple strings in different lines



#List Comprehension

#iterating through list using list comprehension method and removing \n
clean_content=[item.strip("\n" for item in content]

