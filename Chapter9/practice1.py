# Create a class Car with attribute brand = "Scorpio".

class Car:
    brand= "Scorpio"

obj1= Car()
print("Brand name is - ", obj1.brand)



class Car:
  def __init__(self, brand):
    self.brand = brand

carBrand = Car("BMW")
print("Car brand is - ", carBrand.brand)