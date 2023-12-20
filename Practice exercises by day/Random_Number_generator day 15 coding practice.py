
import random_number_generator_udf_function

user_input= input("Enter the numbers in the format (lower_bound,upper_bound) such as 2,10: ")
x=random_number_generator_udf_function.rand_Int_number(user_input)

print(x)
