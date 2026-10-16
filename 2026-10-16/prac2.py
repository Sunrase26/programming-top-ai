class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"Транспорт {self.name}"


class Car(Transport):
    def __init__(self, name, fuel_type):
        super().__init__(name)
        self.fuel_type = fuel_type

    def description(self):
        return f"Машина {self.name}, тип топлива: {self.fuel_type}"


class Plane(Transport):
    def __init__(self, name, max_vysota):
        super().__init__(name)
        self.max_vysota = max_vysota

    def description(self):
        return f"Самолет {self.name}, максимальная высота полета: {self.max_vysota} м"


class Bike(Transport):
    def __init__(self, name, speeds_count):
        super().__init__(name)
        self.speeds_count = speeds_count

    def description(self):
        return f"Велосипед {self.name}, количество скоростей: {self.speeds_count}"


# Проверка работы кода
car = Car("Tesla Model 3", "Электричество")
plane = Plane("Boeing 737", 12500)
bike = Bike("Cube Aim", 24)

print(car.description())
print(plane.description())
print(bike.description())
