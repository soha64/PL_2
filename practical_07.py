#17/03/2026

file = open("text.txt", "w")
file.write("Hello this is Soha Khurshid Kazi\n")
file.write("I'm learning file handling in python.\n")
file.close()
print("Data written successfully.\n")

file = open("text.txt", "r")
content = file.read()
print("Content of the file:")
print(content)
file.close()

fil = open("text.txt", "a")
fil.write("This is an additional line.\n")
fil.close()
print("Data appended successfully.\n")


file = open("text.txt", "r")
content = file.read()
print("Updated content of the file:")
print(content)
file.close()
