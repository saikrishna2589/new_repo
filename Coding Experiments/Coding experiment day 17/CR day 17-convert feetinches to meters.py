def convert_fluid_mm(user_input):
    fluid_to_mm = user_input * 29.57353
    return fluid_to_mm


# user enters input and we convert to int
user_input = float(input("Enter the fluid ounce value to convert to mm: "))

print(convert_fluid_mm(user_input))
