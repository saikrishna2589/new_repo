
from modules.BEday14Parsefunctioncode import parse, convert

' You can also do from modules import BEday14Parsefucntioncode and then do BEday14Parsefucntioncode.parse(feet_inches)'
' and so on whereever function is used '

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")