import json

with open ('questions.json','r') as quiz_questions:
    reading_data=quiz_questions.read()


# the below json.loads mean we load string into the json.loads function so it can turn string into list
# we cant directly print(reading_data) from above open () function as the output is string.
#hence we need to convert it to JSON to work on the program
print(type(reading_data))
print(reading_data)

# converting from string format to a list.THis means we can extract items from the list (as in list of dictionaries)
# unlike when the data strcuture
# was a string

data=json.loads(reading_data)
print(type(data))

for question in data:
    print(question["question_text"])
    for index,option in enumerate(question["options"]):
        print(f"{index+1}.{option}")
    user_feedback= int(input("Enter your option: 1,2,3 or 4 : "))
    question["user_entry"]=user_feedback

score=0
for index,question in enumerate(data):
    if question["user_entry"] == question["correct_answer"]:
        score = score + 1
        result="Correct Answer"
    else:
        result="Wrong Answer"

    message=(f"{result}. your answer : {question['user_entry']}."\
             f" Correct answer:{question['correct_answer']}")
    print(f"q{index+1}.{message}")


print("your score is: " + str(round(score*1.0/len(data)*100.0))+"%")