from matrix import Matrix
import file as File
import util as Util

def toInt(elem):
    return int(elem)

class Mask(object):
    def __init__(self, path):
        super(Mask, self).__init__()
        self.initialize(path)

    def initialize(self, path):
        mask_file = File.read(path)
        dimen = mask_file[0].split() 
        self.width, self.height = [ int(x) for x in dimen]
        self.a = int((self.width - 1) / 2)
        self.b = int((self.height - 1) / 2)
        data = mask_file[1:]
        filtered_data = list(map(toInt, data))
        matrix = Matrix(self.width, self.height, filtered_data)
        self.mask = matrix.getMatrixData()
        self.weight = self.width * self.height
        print("Mask: {}, Weight: {}".format(self.mask, self.weight))

    def getAB(self):
        return (self.a, self.b)
    
    def getDimen(self):
        return (self.width, self.height)

    def getData(self):
        return self.mask

    def getWeight(self):
        return self.weight