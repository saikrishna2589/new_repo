# Task--> Create files based on individual filenames list

# assign the data for each of the file based on text_to_write_string

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
text_to_write = ['Hello', 'Hello', 'Hello']


#using zip function to create a list of tuples for individual objects in filenames and text_to_write
#providing the filepath (..--> going back to root directory and navigating from there to where files need to be
#created. creating files in write mode and data to be written is in the 'text' object within text_to_write list
for filename, text in zip(filenames, text_to_write):
    filepath = f"../Coding exercise 6/{filename}"
    create_file = open(filepath, 'w')
    data_to_be_written = create_file.writelines(text)
    create_file.close()
