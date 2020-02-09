from mask import Mask

def media(mask, data):
    value = sum(data)
    weight = mask.getWeight()
    return round(value / weight)

def median(mask, data):
    data.sort(reverse = False)
    lenght = len(data)
    index = (round(lenght/2) + 1) - 1
    if(lenght > index >= 0):
        return data[index]
    return data[0]

def delation(_, data):
    value = sum(data)
    return 1 if value != 0 else 0

def erosion(_, data):
    value = sum(data)
    return 1 if value == 4 else 0

def moveMask(mask, matrix, effect):
    width, height = matrix.getDimen()
    data = matrix.getMatrixData()
    def func(i, j, elem):
        a, b = mask.getAB()
        dataMask = mask.getData()
        aux = []
        for s in range(-a, a + 1):
            for t in range(-b, b + 1):
                aux_i, aux_j = i + s, j + t
                if(width > aux_j >= 0 and height > aux_i >= 0):
                    aux += [dataMask[s + a][t + b] * data[aux_i][aux_j]]
        if(effect != None):
            return effect(mask, aux)
        return abs(sum(aux))
    return func

def negative(i, j, elem):
    return abs(elem - 1)

def threshold(limiar):
    def func(i, j, elem):
        return 1 if elem > limiar else 0
    return func

def applyDilation(mask, matrix):
    mask.show('Dilation')
    data = matrix.map(moveMask(mask, matrix, delation))
    matrix.setMatrixData(data)
    print('Applied Dilation')

class Manipulator(object):
    def __init__(self, pbm):
        super(Manipulator, self).__init__()
        self.initialize(pbm)

    def initialize(self, pbm):
        self.pbm = pbm

    # para aplicar mascaras que so necessitam da soma dos valores (ex: Laplace e Sobel)
    def applyGenericMask(self, mask):
        mask.show('Generic Mask')
        matrix = self.pbm.getMatrix()
        data = matrix.map(moveMask(mask, matrix, None))
        matrix.setMatrixData(data)
        print('Applied Generic Mask')

    def applyMedia(self, mask):
        mask.show('Media')
        matrix = self.pbm.getMatrix()
        data = matrix.map(moveMask(mask, matrix, media))
        matrix.setMatrixData(data)
        print('Applied Media')

    
    def applyMedian(self):
        mask = Mask('Mascaras/mask-median.txt')
        mask.show('Median')
        matrix = self.pbm.getMatrix()
        data = matrix.map(moveMask(mask, matrix, median))
        matrix.setMatrixData(data)
        print('Applied Median')

    def applyDilation(self, mask):
        mask.show('Dilation')
        matrix = self.pbm.getMatrix()
        data = matrix.map(moveMask(mask, matrix, delation))
        matrix.setMatrixData(data)
        print('Applied Dilation')

    def applyErosion(self, mask):
        mask.show('Erosion')
        matrix = self.pbm.getMatrix()
        data = matrix.map(moveMask(mask, matrix, erosion))
        matrix.setMatrixData(data)
        print('Applied Erosion')
    
    def applyNegative(self):
        matrix = self.pbm.getMatrix()
        data = matrix.map(negative)
        matrix.setMatrixData(data)
        print('Applied Negative')
    
    def applyThreshold(self, limiar):
        matrix = self.pbm.getMatrix()
        data = matrix.map(threshold(limiar))
        matrix.setMatrixData(data)
        print('Applied Threshold')
        
