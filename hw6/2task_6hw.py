class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calc_mas_asfalt(self):
        return self._length * self._width * 25 * 5 / 1000


new_road = Road(20, 5000)
print(f'Необходимо: {new_road.calc_mas_asfalt()} тонн асфальта')
