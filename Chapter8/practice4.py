# Print how many lines are present in notes.txt

try:
    with open("Chapter8/notes.txt", "r") as f:
        listOfLines= f.readlines()
        print("Output of readLines Function", listOfLines)
        print("Number of Lines in File", len(listOfLines))
except:
    print("That files does not exist")

# RENAMING THE FILE 

import os 
# os.rename("Chapter8/khushi.txt", "Chapter8/report.txt") # This will rename the file khushi.txt to report.txt
# os.remove("Chapter8/khushi.txt") # This will delete the file khushi.txt. Be careful while using this command. It will delete the file permanently.