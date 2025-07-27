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
        return self.__brand + "!"
    
    @staticmethod
    def general():
        print("Hello From Static Method ")

    @property
    def model(self):
        return self.__model
        
class Baterry():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def get_battery_size(self):
        return self.battery_size

class Engine():
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def get_engine_type(self):
        return self.engine_type
    
class ElectricCar(Car, Baterry, Engine):
    def __init__(self,brand,model,battery_size, engine_type=None):
        super().__init__(brand,model)
        self.battery_size = battery_size
        self.engine_type = engine_type

my_electric_car1 = ElectricCar("Audi","xyz","200 kWh","Desiel")
my_electric_car2 = ElectricCar("Tesla", "Model S", "100 kWh", "Electric")

print(my_electric_car1.get__brand())
print(my_electric_car1.battery_size) 
print(my_electric_car1.engine_type)
print(f"The {my_electric_car1.get__brand()} car is {my_electric_car1.get_engine_type()} type with a battery size of {my_electric_car1.get_battery_size()}.")

electric_cars = [my_electric_car1, my_electric_car2]

for car in electric_cars:
    print(f"Brand: {car.get__brand()}, Model: {car.model}, Battery Size: {car.battery_size}, Engine Type: {car.engine_type}")

print(isinstance(my_electric_car1, ElectricCar))
print(isinstance(my_electric_car1, Car))

# my_electric_car.dispaly()
# print(my_electric_car.get__brand())

# c1 = Car("Audi","xyz")
# c2 = Car("Tata","Safari")
# c3 = Car("abc","xyz")

# c2.model = "nano"

# c1.dispaly()
# c2.dispaly()
# print(c2.model)
# print(c1.carCount)
print(Car.carCount)
# print(c1.brand)
# print(c1.model)

print(Car.general())  


