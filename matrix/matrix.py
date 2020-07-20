class Matrix:
    def __init__(self, matrix_string):
        matrix_list = matrix_string.split('\n')[1:-1]
        self.matrix = [[int(j) for j in i.split()] for i in matrix_list]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        pass

Matrix('''
1 2 3
2 3 4
3 4 5
''')
