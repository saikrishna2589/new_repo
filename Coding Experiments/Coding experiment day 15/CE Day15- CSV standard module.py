
# Here we are importing CSV standard module and reading data from a csv file available in the same directory
# csvreader is a function within csv module and it expects the file object as input
#csv.reader acually gives iteratory object that is not readable. Therefore we convert to a list format using 'list'
#function so data is stored as list

import csv
with open("weather.csv", 'r') as csv_file:
    data=list(csv.reader(csv_file))

print(data)


type_which_city=input("which city's temperature you want to see?: ")

for city_and_temp in data:
    city_name= city_and_temp[0].strip()
    if city_name == type_which_city.strip():
        temperature= city_and_temp[1].strip('" "')
        print(f"Temperature in {city_name} is {temperature}")
        break

else:
    print(f"city name provided not in database")

