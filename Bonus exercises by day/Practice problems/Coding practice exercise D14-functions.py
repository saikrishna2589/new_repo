
temperatur e =input("whats the current water temperature?:")
temperatur e =float(temperature)

def water_state(temperature=99):
    if temperature <= 0:
        output = "Solid"
    elif 0 < temperature < 100:
        output = "Liquid"
    else:
        output = "Gas"
    return output

water_temperatur e =water_state(temperature)
messag e= f" water temperature is in {water_temperature} form"


print(message)






