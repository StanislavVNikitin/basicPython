import time


class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self):
        i = 0
        while True and i < 10:
            self.__color = "Красный"
            print(self.__color)
            time.sleep(7)
            self.__color = "Желтый"
            print(self.__color)
            time.sleep(2)
            self.__color = "Зеленый"
            print(self.__color)
            time.sleep(10)
            i += 1


t = TrafficLight()
t.running()
