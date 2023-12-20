# question-convert the height from feet and inches to meters

height_feet_inches = input("Enter your height in feet and inches: ")


def convert(height_feet_inches):
    feet_inches = height_feet_inches.split(" ")
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])

    meters = feet * 0.3048 + inches * 0.00254
    return meters  # decoupling concept--. use the value as a return rather than string or complex string.


# as output may be used going forward in the program


height_feet = convert(height_feet_inches)
print(height_feet)

feet_provided = height_feet_inches.split(" ")[0]
inches_provided = height_feet_inches.split(" ")[1]

height_and_feet_provided = f"your height in {feet_provided} feet and {inches_provided} inches is equal to {height_feet} meters"
print(height_and_feet_provided)

if height_feet < 1:
    print("sorry,you can't use the slides")
else:
    print("please go ahead and use the slides")

`