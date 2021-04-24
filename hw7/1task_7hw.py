class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for row in self.matrix_list:
            for x in row:
                print("{:4d}".format(x), end="")
            print()
        return ''

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix_list)):
            new_matrix.append([])
            for j in range(len(other.matrix_list[i])):
                new_matrix[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
        return Matrix(new_matrix)


new_matrix_1 = Matrix([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
new_matrix_2 = Matrix([[5, 8, 1], [6, 7, 3], [4, 5, 9]])
new_matrix_3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(new_matrix_1 + new_matrix_2 + new_matrix_3)
