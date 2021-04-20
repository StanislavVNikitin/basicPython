class Stationery:

    def __init__(self, t="Default Stationery"):
        self.title = t
        self.draw()

    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отрисовки как ручки.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отрисовки как карандаша.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отрисовки как маркера.')


unit_stationery = Stationery()
unit_pen = Pen("Ручка")
unit_pencil = Pencil("Карандаш")
unit_handle = Handle("Маркер")
