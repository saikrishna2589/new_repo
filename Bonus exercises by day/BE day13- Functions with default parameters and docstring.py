# question-the local variables 'feet' and 'inches' cannot be accessed outside so custom f string messages outside
# functions are not easy to create . so we need to decouple the BE day 12 function created into 2 functions .one for
# parsing the user input and the other for converting the height into meters convert the height from feet and inches
# to meters

height_feet_inches = input("Enter your height in feet and inches: ")


# so bottom line-one function to parse the data and return the feet and inches to use it outside the function.
# 2nd function is to convert the ft and inches parsed into metres calculation.
# function needs to do 1 thing well so don't include parsing and converting in same function. rather split both of these
# into 2 functions

def parse_height(height_feet_inches):
    feet_inches = height_feet_inches.split(" ")
    feet = float((feet_inches[0].strip(" ")))
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}  # returning in dictionary format


# making height in ft and inches accessible outside the function now by returning the values in tuple format
height_in_ft_and_inches = parse_height(height_feet_inches)
feet_ft = height_in_ft_and_inches["feet"]  # access the dictionary elements
inches_in = height_in_ft_and_inches["inches"]


def convert_ft_m3():
    meters = float(feet_ft) * 0.3048 + float(inches_in) * 0.0254
    return meters


height_feet_m3 = convert_ft_m3()
print(height_feet_m3)

feet_provided = feet_ft
inches_provided = inches_in

height_and_feet_provided = f"your height in {feet_provided} feet and {inches_provided} inches is equal to {height_feet_m3} meters"
print(height_and_feet_provided)

if height_feet_m3 < 1:
    print("sorry,you can't use the slides")
else:
    print("please go ahead and use the slides")
