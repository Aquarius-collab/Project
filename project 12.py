f = open("sample.txt", "w")
f.write("Hello Students\nWelcome to File Handling in Python")
f.close()

f = open("sample.txt", "r")
print("Full Read:")
print(f.read())
f.close()

f = open("sample.txt", "r")
print("\nLine by Line:")
for line in f:
    print(line.strip())
f.close()

f = open("sample.txt", "a")
f.write("\nThis line is added using append mode.")
f.close()

f = open("sample.txt", "r")
print("\nAfter Append:")
print(f.read())
f.close()

f = open("sample.txt", "w")
f.write("File overwritten. Previous content removed.")
f.close()

f = open("sample.txt", "r")
print("\nCursor Position:", f.tell())
print("Reading:", f.read())
f.seek(0)
print("After Seek:", f.read())
f.close()