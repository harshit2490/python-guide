# Write a program to read a text from a given file certificate.txt
# and find whether it contains the word live.

file= open("Chapter8/certificate.txt", "r")
dataOfFile= file.read()

print("Data of the file is: ", dataOfFile)
dataOfFile= dataOfFile.lower()
print("Data of the file in lower case is: ", dataOfFile)

if "live" in dataOfFile:
    print("Yes Live word is present in the file")
else:
    print("No")
