class Matrix(object):
    def __init__(self, width, height, values):
        super(Matrix, self).__init__()
        self.initialize(width, height, values)

    def initialize(self, width, height, values):
        self.width = width
        self.height = height
        self.matrix = []
        self.transposed = []
        for i in range(0, height):
            line = []
            for j in range(0, width):
                index = j + (i * width)
                line += [values[index]]
            self.matrix += [line]
    
    def getDimen(self):
        return (self.width, self.height)

    def setMatrixData(self, matrix):
        self.matrix = matrix

    def getMatrixData(self):
        return self.matrix

    def getTransposed(self):
        if(self.transposed == []):
            for j in range(0, self.width):
                column = []
                for i in range(0, self.height):
                    column += [self.matrix[i][j]]
                self.transposed += [column]
        return self.transposed
    
    def map(self, func):
        aux = []
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                elem = self.matrix[i][j]
                line += [func(i, j, elem)]
            aux += [line]
        return aux
    
    def sum(self):
        aux = 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                aux += self.matrix[i][j]

        return aux

    def show(self):
        for line in self.matrix:
            for x in line:
                print(x, end=' ')
            print()

