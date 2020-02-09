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
        columns = matrix.getTransposed()
        self.numLines = Util.calculateLineOrColumn(lines)
        self.numColumns = Util.calculateLineOrColumn(columns)
        self.numWords = 0

    def getNumberOfLinesAndColumns(self):
        return (self.numLines, self.numColumns)

    def showInfo(self):
        print("Lines: {}, Columns: {}, Words: {}".format(
            self.numLines,
            self.numColumns, 
            self.numWords))