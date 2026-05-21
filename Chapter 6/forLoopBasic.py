# Iterating through a list using a for loop
foodList= ["cake", "mango", "pizza"]

for item in foodList:
    print(item)

# Itrating through a tuple using a for loop
collegesTuple = ("NIT-Delhi", "ABES", "BBAU", "IIT-D", "IIT-H")

for eachItem in collegesTuple:
    print("Colleges Visited by Harshit" , eachItem)

# Iterating through a dictionary using a for loop
carRatedDict = {
    "BMW": 4.5,
    "Audi": 4.0,
    "Mercedes": 4.8,
    "Tata": 3.5,
    "Maruti": 3.8,
}
for eachKey in carRatedDict:
    print(f"Car Name: {eachKey}, Rating: {carRatedDict[eachKey]}")


# If you want to access both the index and the item in a list, you can use the enumerate() function.
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)