from abc import ABC, abstractmethod


class Warehouse():

    def __init__(self):
        self._dict = {}

    def add_to_warehouse(self, equipment):
        if not equipment.get_error():
            self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract_warehouse(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @classmethod
    def find_to_warehouse(cls, name_obj):
        return OfficEquipment.find(name_obj)

    @abstractmethod
    def action(self):
        pass


class OfficEquipment(Warehouse):

    def __init__(self, in_num, place_of_storage, type_teh, name, count):
        super().__init__()
        self.error = False
        self.in_num = in_num
        self.place_of_storage = place_of_storage
        self.type_teh = type_teh
        self.name = name
        self.count = 0
        try:
            self.count = int(count)
        except(ValueError, TypeError) as err:
            self.error = True
            print(
                f'Введено не число в количестве передаваемой техники на склад: {count}, принтер {name} не может быть передан на склад!')

        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def get_error(self):
        return self.error

    def find(self):
        return f'{self.type_teh} название {self.name} находится в стелаже {self.place_of_storage}'

    def __repr__(self):
        return f'{self.type_teh}: {self.name}, Ин.ном: {self.in_num}, кол: {self.count} '


class Printer(OfficEquipment):

    def __init__(self, in_num, place_of_storage, name, count, format_papper, color_print):
        type_teh = "Принтер"
        super().__init__(in_num, place_of_storage, type_teh, name, count)
        self.format_papper = format_papper
        self.color_print = color_print

    def action(self):
        return 'Печатает...'


class Scanner(OfficEquipment):

    def __init__(self, in_num, place_of_storage, name, count, scan_resolution):
        type_teh = "Сканер"
        super().__init__(in_num, place_of_storage, type_teh, name, count)
        self.scan_resolution = scan_resolution

    def action(self):
        return 'Сканирует'


class Copier(OfficEquipment):

    def __init__(self, in_num, place_of_storage, name, count, copy):
        type_teh = "Копир"
        super().__init__(in_num, place_of_storage, type_teh, name, count)
        self.copy = copy

    def action(self):
        return 'Копирует'


warehouse = Warehouse()
printer_hp = Printer(101, "A1", "HP 277", '3', "A4", True)
warehouse.add_to_warehouse(printer_hp)
scanner_canon = Scanner(102, "A2", "Canon Pixma 304", 5, "4500")
warehouse.add_to_warehouse(scanner_canon)
copier_xerox = Copier(103, "A3", "Xerox 205", 3, "50000")
warehouse.add_to_warehouse(copier_xerox)
printer_kyocera1 = Printer(104, "A4", "Kyocera M2135", 1, "A4", False)
warehouse.add_to_warehouse(printer_kyocera1)
printer_kyocera2 = Printer(105, "A5", "Kyocera TaskAlfa 2551ci", 'g', "A3", True)
warehouse.add_to_warehouse(printer_kyocera2)
print('****Текущий список техники на складе****')
print(warehouse._dict)
print('****Текущий список техники на складе после выдачи Scanner****')
warehouse.extract_warehouse('Scanner')
print(warehouse._dict)
print(f'Поиск на складе техники: ')
print(warehouse.find_to_warehouse(printer_hp))
