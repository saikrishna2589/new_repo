#open the file and removing the text header
with open('../Bonus exercises by day/data.txt', 'r') as data1:
    file_opening = data1.readlines()[1:]

print(file_opening)

# calculate the sum of the numbers in the list
def total_sum_calc(sum_of_values=0):
    for f in file_opening:
        f=f.strip()
        sum_of_values = sum_of_values + int(f)
    return sum_of_values

#take the average
total_average=int(total_sum_calc())/len(file_opening)
print(total_average)