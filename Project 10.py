file = open("students.txt", "w")
file.write("Roy - Favourite Subject: Maths\n")
file.write("Sneha - Favourite Subject: Science\n")
file.write("Karan - Favourite Subject: English\n")
file.close()

file = open("students.txt", "a")
file.write("Aisha - Favourite Subject: Social Studies\n")
file.write("Manoj - Favourite Subject: Computer\n")
file.close()

file = open("students.txt", "r")
content = file.read()
print("Student Details:\n")
print(content)
file.close()






