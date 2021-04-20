class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        print(self.get_full_name())
        print(self.get_total_income())

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return float(self._income.get("wage")) + float(self._income.get("bonus"))


cio_persone = Position("Ivan", "Ivanov", "CIO", 170000, 50000)
ingener_persone = Position("Petr", "Smirnov", "Ingener", 100000, 30000)
