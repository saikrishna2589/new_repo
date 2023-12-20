

import datetime
current_date=datetime.datetime.now().strftime('%d-%m-%Y')
enter_today_date = input("Enter today's date: ")
enter_mood_rating = input("Enter your mood rating? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../Journal/{current_date}.txt", 'a') as today_file:
    today_file.write(f"Today's date is: {enter_today_date}\n")
    today_file.write(f"My mood rating: {enter_mood_rating}\n")
    today_file.write(f"My thoughts for today are: {thoughts}\n ")

print(f" Data has been appended to file {current_date}.txt")

with open(f"../Journal/{current_date}.txt",'r')as today_file_data:
    today_file_data_show=today_file_data.readlines()
    print(today_file_data_show)