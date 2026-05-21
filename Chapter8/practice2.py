# Open a file called report.txt in write mode.


# This will create a new file with the name report.txt and open it in write mode. If the file already exists, it will overwrite the existing content.
file= open("Chapter8/report12.txt", "w") 
file.write("Mai toh majak kar raha thi")


# This will create a new file with the name report87979768.txt and open it in write mode. If the file already exists, it will raise a FileExistsError.
file= open("Chapter8/report13.txt", "x")
file.write("Mai toh majak kar raha thi")
