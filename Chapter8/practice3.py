# Read only the first line of bio.txt

with open("Chapter8/bio.txt", "r") as f:
    line1= f.readline()
    print("Line 1", line1)
    line2= f.readline()
    print("Line 2", line2)
    line3= f.readline()
    print("Line 3", line3)

