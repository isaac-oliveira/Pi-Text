import util as Util

class Text(object):
    def __init__(self, pbm):
        super().__init__()
        self.initialize(pbm)

    def initialize(self, pbm):
        self.pbm = pbm
        self.calculateLinesAndColumns()

    def calculateLinesAndColumns(self):
        matrix = self.pbm.getMatrix()
        width, height = matrix.getDimen()
        lines = matrix.getMatrixData()
        self.numLines = Util.calculateLineOrColumn(lines)
        self.numColumns = 0
              
        print("Num Lines: ")
        print(self.numLines)


    def getNumberOfLinesAndColumns(self):
        return (self.numLines, self.numColumns)
