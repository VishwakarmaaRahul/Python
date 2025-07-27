class Car:
    carCount =0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.carCount += 1
    
    def dispaly(self):
        print(self.__brand,self.__model)
        # return f"{self.brand}{" "}{self.model}"
    
    def get__brand(self):
        return self.__brand + " !"
    
    @staticmethod
    def general():
        print("Hello From Static Method ")

    @property
    def model(self):
        return self.__model
        

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size




my_electric_car = ElectricCar("Tesla","xyz","100")
my_electric_car.dispaly()
print(my_electric_car.get__brand())

c1 = Car("Audi","xyz")
c2 = Car("Tata","Safari")
c3 = Car("abc","xyz")

c2.model = "nano"

c1.dispaly()
c2.dispaly()
print(c2.model)
print(c1.carCount)
print(Car.carCount)
print(c1.brand)
print(c1.model)

print(Car.general())  