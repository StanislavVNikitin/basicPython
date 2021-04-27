class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел ({self.a} + {self.b}i) + ({other.a} + {other.b}i) равна: {"" if(self.a + other.a) < 0 else ""}{self.a + other.a} {"+" if (self.b + other.a) >0 else "-"} {self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел ({self.a} + {self.b}i) * ({other.a} + {other.b}i) равна: {"-" if (self.a * other.a - (self.b * other.b))< 0 else ""}{self.a * other.a - (self.b * other.b)} {"+" if self.b * other.a >0 else "-"} {abs(self.b * other.a)}i'

com_num1 = ComplexNum(-1, -2)
com_num2 = ComplexNum(2, 4)
print(com_num1  + com_num2)
print(com_num1  * com_num2)