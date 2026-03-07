# contents = ['All carrots are to be sliced longitudinally.', 'The carrots were reportedly sliced.', 'The slicing process was well presented.' ]
#
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for content, filename in zip(contents, filenames):
#     file = open(f"files/{filename}", 'w')
#     file.write(content)

# Another example
# member = input("Add a new member: ") + "\n"
# file = open("files/members.txt", "r")
# members = file.readlines()
# file.close()
#
# members.append(member)
#
# file = open("files/members.txt", "w")
# file.writelines(members)
# file.close()

#Another example
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     file = open(filename, "w")
#     file.write("Hello and Goodbye!")
#     file.close()

#Another example
files = ["a", "b", "c"]
for file in files:
    new = open(f"{file}.txt", "w")
    new.write(f"I am {file}.")
    new.close()