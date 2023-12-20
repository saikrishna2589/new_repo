# reading the file within custom function and removing the text header
def get_average():
    with open(r'/Bonus exercises by day/data.txt', 'r') as data1:
        file_opening = data1.readlines()

        # better to have intermediate variable rather than slicing at time of
        # reading the data.  slicing done separate to reading is better
    values = file_opening[1:]

    # using list comprehension method to convert strings (and remove new lines)
    # with float and replacing the same variable to get new format
    values = [float(v.strip()) for v in values]

    # calculating the average
    average_local = sum(values) / len(values)

    # returning the average
    return average_local


# output
average = get_average()
print(average)
