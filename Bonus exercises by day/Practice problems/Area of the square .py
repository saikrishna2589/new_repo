dim_of_square=input("enter one of the dimensions of square: ")
dim_of_square=float(dim_of_square)

def get(dim_of_square):
    area_of_square=dim_of_square*dim_of_square
    return  area_of_square

area_of_the_square=get(dim_of_square)
print(f"Area of the square is {area_of_the_square} m2")