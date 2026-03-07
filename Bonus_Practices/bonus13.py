#decoupling of functions from previous bonus

feet_inches = input("Enter feet in inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
print("fi", f, i)
result = convert(f, i)

if result < 1 :
    print("Kids is not tall enough")
else:
    print("Kid can ride the slide")