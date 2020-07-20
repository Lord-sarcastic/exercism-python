class Matrix:
    def __init__(self, matrix_string):
        matrix_list = matrix_string.split('\n')[1:-1]
        self.matrix = [[int(j) for j in i.split()] for i in matrix_list]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        values = list(zip(*self.matrix))
        return [i for i in values[index - 1]]

