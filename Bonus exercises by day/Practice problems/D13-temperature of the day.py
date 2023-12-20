temperature = input("Enter the temperature: ")
temperature = float(temperature)


def get(temperature):
    output = []
    if temperature > 7:
        output.append("Warm")
    if temperature <= 7:
        output.append("Cold")
    return output


output_temperature = get(temperature)
print(output_temperature)
