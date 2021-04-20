import random


class Car:
    # Атрибуты
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.status = "stop"

    def go(self):
        print(f"{self.name} поехали!")
        self.status = "go"

    def stop(self):
        print(f"{self.name} остановилась:")
        self.status = "stop"

    def turn(self, direction):
        print(f"{self.name} поворачивает на {direction}")

    def show_speed(self):
        if self.status == "go":
            print(f"{self.name} едет со скоростью {self.speed} км/ч")
        else:
            print(f"{self.name} стоит")

    def is_polise_car(self):
        if self.is_police == True:
            print("Полицейская машина!!!")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.__speed_max = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_max:
            print(f"ВНИМАНИЕ!!! {self.name} едет с превышением скорости в {self.speed - self.__speed_max} км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.__speed_max = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_max:
            print(f"ВНИМАНИЕ!!! {self.name} едет с превышением скорости в {self.speed - self.__speed_max} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


town_car = TownCar(random.randint(50, 80), "black", "Ford")
town_car.is_polise_car()
town_car.go()
town_car.show_speed()
town_car.turn("право")
town_car.turn("лево")
town_car.stop()
print()
work_car = WorkCar(random.randint(20, 50), "red", "DAW")
work_car.is_polise_car()
work_car.go()
work_car.show_speed()
work_car.turn("право")
work_car.turn("лево")
work_car.stop()
print()
police_car = PoliceCar(random.randint(90, 150), "blue", "AudiPolice")
police_car.is_polise_car()
police_car.go()
police_car.show_speed()
police_car.turn("лево")
police_car.turn("право")
police_car.stop()
print()
sport_car = SportCar(random.randint(100, 140), "green", "Lanbargine")
sport_car.is_polise_car()
sport_car.go()
sport_car.show_speed()
sport_car.turn("лево")
sport_car.turn("право")
sport_car.stop()
