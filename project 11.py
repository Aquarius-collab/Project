print("1. Using read():")
with open("students.txt", "r") as file:
    data = file.read()
    print(data)

print("\n----------------------------\n")

print("2. Using readline():")
with open("students.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

print("\n----------------------------\n")

print("3. Using readlines():")
with open("students.txt", "r") as file:
    lines = file.readlines()
    print(lines)

print("\n----------------------------\n")

print("4. Using for loop:")
with open("students.txt", "r") as file:
    for line in file:
        print(line)






