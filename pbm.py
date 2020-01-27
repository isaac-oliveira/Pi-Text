from matrix import Matrix
import file as File
import util as Util

class Pbm(object):
    def __init__(self, path):
        super(Pbm, self).__init__()
        self.initialize(path)
    
    def initialize(self, path):
        self.pbm = File.read(path)
        dimen = self.pbm[2].split() 
        self.width, self.height = [ int(x) for x in dimen]
        pixels = self.pbm[3:]
        filtered_pixels = Util.filterData(pixels)
        print(len(filtered_pixels))
        self.matrix = Matrix(self.width, self.height, filtered_pixels)

    def matrixToPbm(self, matrix):
        data = self.getMatrix().getMatrixData()
        dimen = '{} {}'.format(self.width, self.height)
        aux = ['P1', '# Isaac', dimen]
        for i in range(0, self.height):
            aux_line = ''
            for j in range(0, self.width):
                elem = data[i][j]
                end = ' ' if j != self.width - 1 else ''
                aux_line += '{}{}'.format(elem, end)

            aux += [aux_line]

        return aux

    def save(self, name):
        filename = name + '.pbm'
        matrix = self.getMatrix()
        data = matrix.getMatrixData()
        self.pbm = self.matrixToPbm(data)
        File.write(self.pbm, filename)

    def getDimen(self):
        return (self.width, self.height)

    def getMatrix(self):
        return self.matrix