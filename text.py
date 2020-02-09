import util as Util
import matrix as Matrix
from mask import Mask
import manipulator as Manipulator
import copy

class Text(object):
    def __init__(self, pbm):
        super().__init__()
        self.initialize(pbm)

    def initialize(self, pbm):
        self.pbm = pbm
        self.calculateLinesAndColumns()

    def calculateLinesAndColumns(self):
        self.matrix = self.pbm.getMatrix()
        width, height = self.matrix.getDimen()
        lines = self.matrix.getMatrixData()
        columns = Matrix.getTransposed(lines, width, height)
        self.numLines = Util.calculateLineOrColumn(lines)
        self.numColumns = Util.calculateLineOrColumn(columns)
        self.positionWord = self.getWordPostion()
        self.numWord = len(self.positionWord)

    def getWordPostion(self):
        aux = []
        width, height = self.matrix.getDimen()
        matrix_copy = copy.copy(self.matrix)
        mask = Mask('Mascaras/mask-dilation5x5.txt')
        Manipulator.applyDilation(mask, matrix_copy)
        lines = matrix_copy.getMatrixData()
        positionLines = self.getInitialAndFinal(lines)
        for l_initial, l_final in positionLines:
            columns = Matrix.getTransposed(lines[l_initial:l_final + 1], width, l_final - l_initial)
            positionColumns = self.getInitialAndFinal(columns)
            for c_initial, c_final in positionColumns:
                aux += [((l_initial, c_initial), (l_final, c_final))]
                
        return aux

    def markWords(self):
        data = self.matrix.getMatrixData()
        for posI, posF in self.positionWord:
            x_i, y_i = posI
            x_f, y_f = posF
            for i in range(y_i, y_f + 1):
                data[x_i][i] = 1
            for i in range(y_i, y_f + 1):
                data[x_f][i] = 1
            for i in range(x_i, x_f + 1):
                data[i][y_i] = 1
            for i in range(x_i, x_f + 1):
                data[i][y_f] = 1

        self.matrix.setMatrixData(data)

    def getInitialAndFinal(self, data):
        aux = []
        space = True
        initial = 0
        final = 0
        for i, elem in enumerate(data):
            sumElem = sum(elem)
            if(space and sumElem != 0):
                aux_i = i - 2
                initial = aux_i
                space = False
            elif(not space and sumElem == 0):
                final = i + 2
                aux += [(initial, final)]
                space = True

        return aux

    def getNumberOfLinesAndColumns(self):
        return (self.numLines, self.numColumns)

    def showInfo(self):
        print("Lines: {}, Columns: {}, Words: {}".format(
            self.numLines,
            self.numColumns,
            self.numWord
        ))
