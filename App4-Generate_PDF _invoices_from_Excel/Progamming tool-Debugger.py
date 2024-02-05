message="Hello"
def get_frequency(text, word):
    # converting text to list of individual elements of the variable text
    words = text.split(" ")
    # counting how many times "love" word appears in the list
    count = words.count(word)

    # frequency of the specific word divide by total number of words in the list
    frequency_ratio = count / len(words) * 100
    return frequency_ratio


frequency= get_frequency("Hello baby,how are you today baby? whats your plan baby","baby")

if frequency>5:
    print("High frequency")
else:
    print("Low frequency")

print(message)