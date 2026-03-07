password = input("Enter your password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)


digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)

print(result)
if all(result):
    print("Strong Password")
else:
    print("Weak Password")

#-----------------Using a dictionary
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result["digits"] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
# result["upper-case"] = uppercase
#
# print(result)
#print(result.values())

# if all(result.values()):
#     print("Strong Password")
# else:
#     print("Weak Password")