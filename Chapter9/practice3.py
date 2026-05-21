# Create class Student that takes 3 marks and has a method average().

class Student:
    def __init__(self, name, listOfMarks):
        self.name= name
        self.listOfMarks= listOfMarks

    def average(self):
        sum= 0
        for eachValue in self.listOfMarks:
            sum= sum+eachValue

        average= sum/3
        print("Average is: ", average)


name = input("Enter the name of student: ")
totalSubjects= int(input("Enter total subjects: "))

listOfMarks = []
for i in range(totalSubjects):
    print(f"Enter marks for subject {i+1}: ")
    mark = float(input())
    listOfMarks.append(mark)

student1= Student(name, listOfMarks)
student1.average()