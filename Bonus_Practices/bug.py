# buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
# for first, second, third in buttons:
#     print(first, second, third)


#================================================
# with open("file.txt", 'r') as file:
#     content = file.read()
#     print(content)
#     print(len(content))

#====================================================
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

#===========================================================
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

#==============================================================
# def get_nr_items(user_input):
#     words = user_input.split(",")
#     return len(words)
#
#
# get_nr_items("john,lisa, teresa")
# print(get_nr_items("john,lisa, teresa"))

#===================================================================
def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(1000)
print(time)