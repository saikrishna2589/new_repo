
sentence=str(input("Enter your Phrase: "))
def count_period(sentence):
    count_of_periods=sentence.count('.')
    return count_of_periods

period_count=count_period(sentence)
print(f"The number of periods in your sentence is {period_count}")