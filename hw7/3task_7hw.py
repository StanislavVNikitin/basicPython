class Cell:

    def __init__(self, num_cell):
        self.num_cell = num_cell
        self.tmp_cell = 0
        self.result = ""

    def __str__(self):
        return f'{self.num_cell}'

    def make_order(self):
        self.result = ""
        i = 0
        len_cell = self.num_cell // 5
        len_div_cell = self.num_cell % 5
        while i < len_cell:
            self.result += "*" * 5 + "\n"
            i += 1

        if len_div_cell > 0:
            self.result += "*" * len_div_cell

        return f'{self.result}'

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        if self.num_cell > 0:
            return Cell(self.num_cell - other.num_cell)
        else:
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __truediv__(self, other):
        result = self.num_cell // other.num_cell
        if result > 0:
            return Cell(result)
        else:
            return Cell(0)


new_cell_1 = Cell(12)
new_cell_2 = Cell(7)
new_cell_3 = Cell(9)

print(new_cell_1)
print(new_cell_1.make_order())

print()
print(new_cell_2)
print(new_cell_2.make_order())

print()
print(new_cell_3)
print(new_cell_3.make_order())

print()
print(new_cell_1 + new_cell_2 - new_cell_3)
print((new_cell_1 + new_cell_2 - new_cell_3).make_order())

print()
print(new_cell_1 * new_cell_2 / new_cell_3)
print((new_cell_1 * new_cell_2 / new_cell_3).make_order())
