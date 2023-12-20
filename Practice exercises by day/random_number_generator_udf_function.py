#write a program to ask user to enter numbers in the format (2,10) and get a random number
#from within that range
import random
def rand_Int_number(user_input):

    parse_user_input=user_input.split(",")
    lower_bound=int(parse_user_input[0])
    upper_bound=int(parse_user_input[1])
    random_number_generator=random.randint(lower_bound,upper_bound)
    return random_number_generator

