year_of_birth = input("what's your year of birth: ")
year_of_birth=int(year_of_birth)

def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


user_age = f"you are {get_age(year_of_birth)} years old"

print(user_age)
