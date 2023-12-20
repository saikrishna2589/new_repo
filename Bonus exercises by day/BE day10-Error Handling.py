# write a program to calculate volume of a rectangle

while True:
    try:
        height = int(input("Enter the height of the rectangle: "))
        weight = int(input("Enter the weight of the rectangle: "))
        length = int(input("Enter the length of the rectangle: "))

        if height == length:
            print("The dimensions provided are for a square and not a rectangle.Please re-enter the dimensions")
            exit("Bye for now!")
        volume = height * weight * height
        print("volume of the rectangle is: ", volume, "in m3")

        '''elif height == length:
            print("The dimensions provided are for a square and not a rectangle.Please re-enter the dimensions")
            exit("Bye for now!")  # exit() function will break and end the program.Although while True is specified,
            # program ends and user won't be able to enter new inputs again until re-run the program again manually'''

    except ValueError :
        print("please enter the actual dimension in numeric format ")
        continue

