contents = ["All carrots arr sliced",
            "All carrots sliced longitudinally",
            "All carrots sliced latitude wise"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# how do we create multiple files in the folder 'Files' with name of the files in filenames list
# and secondly how to  have the data coming from 'contents' list stored inside these filenames respectively
# we can use 'zip' function ,works similar to enumerate

for c, f in zip(contents, filenames):  # creating a list with tuples.one value from content and the other
    # from filenames
    filepath = f"../Files/{f}"  # create file path on each iteration
    # based on filenames list
    file = open(filepath, 'w')  # create the file on each iteration
    file.write(c)  # write each string from contents list to the file

# extra knowledge--> if you want to split the sting display into multiple lines but it is still one object, use a '\'(
# backslash)
a = "I am a string " \
    "on " \
    "my own"

print(a)
