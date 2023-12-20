# Task - replace the '.' with "-" and add ".txt" at the end
filenames = ["1.doc", "1.report", "1.presentation"]

'''
final_filenames=[]
for filename in filenames:
    updated_filename=filename.replace(".", "-")+".txt"
    final_filenames.append( updated_filename)

print(final_filenames)
'''

# how about we use list comprehension method rather than a traditional method above

transformed_filenames = [filename.replace(".", "-")+".txt" for filename in filenames]
print(transformed_filenames)