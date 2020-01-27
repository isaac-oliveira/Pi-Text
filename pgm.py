from matrix import Matrix
import file as File
import util as Util

def toInt(elem):
    return int(elem)

class Pgm(object):
    def __init__(self, path):
        super(Pgm, self).__init__()
        self.initialize(path)
    
    def initialize(self, path):
        self.pgm = File.read(path)
        dimen = self.pgm[2].split() 
        self.width, self.height = [ int(x) for x in dimen]
        self.tom = int(self.pgm[3])
        pixels = self.pgm[4:]
        filtered_pixels = list(map(toInt, pixels))
        print(len(filtered_pixels))
        self.matrix = Matrix(self.width, self.height, filtered_pixels)

    def matrixToPgm(self, matrix):
        data = self.getMatrix().getMatrixData()
        dimen = '{} {}'.format(self.width, self.height)
        tom = str(self.tom)
        aux = ['P2', '# Isaac', dimen, tom]
        for i in range(0, self.width):
            aux_line = ''
            for j in range(0, self.height):
                elem = data[i][j]
                end = ' ' if j != self.width - 1 else ''
                aux_line += '{}{}'.format(elem, end)

            aux += [aux_line]

        return aux

    def save(self, name):
        filename = name + '.pgm'
        matrix = self.getMatrix()
        data = matrix.getMatrixData()
        self.pgm = self.matrixToPgm(data)
        File.write(self.pgm, filename)

    def getDimen(self):
        return (self.width, self.height)
    
    def getTom(self):
        return self.tom

    def getMatrix(self):
        return self.matrix