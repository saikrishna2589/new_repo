import random

# returns a random floating point between 0 and 1
rand_float_number= random.random()
print(rand_float_number)

lower_bound=int(input("Enter the lower bound value:  "))
upper_bound=int(input("Enter the upper bound value: "))


#1st method
rand_int_number=random.randint(lower_bound,upper_bound)
print(rand_int_number)

#2nd method
rand_range_method= random.randrange(lower_bound,upper_bound)
print(rand_range_method)