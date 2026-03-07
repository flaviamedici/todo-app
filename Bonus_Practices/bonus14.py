#decoupling of functions from previous bonus
from Bonus_Practices.converters_bonus14 import convert
from Bonus_Practices.parsers_bonus14 import parse

feet_inches = input("Enter feet in inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']}, {parsed['inches']} = {result}")

if result < 1 :
    print("Kids is not tall enough")
else:
    print("Kid can ride the slide")