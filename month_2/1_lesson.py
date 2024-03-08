class Car:
    wheels = 4
    def __init__(self,model,year,color):
       self.model = model
       self.year = year
       self.color = color
    def info(self):
     print(f"{self.model}, /n год выпуска -{self.color}, /nцвет - {self.year}")   



mers = Car("w140",1992,"Black")
bmw = Car("bmw - x7",2018,"white")
# audi = Car()
# print(mers.wheels)
# print(bmw.wheels) 
# print(audi.wheels) 
# print(mers.model, mers.color, mers.year)
# print(bmw.model, bmw.color, bmw.year)
mers.info()
