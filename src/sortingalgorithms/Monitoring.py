class Monitor:
    def __init__(self):
        self.numberOfComparisons = 0
        self.numberOfMoves = 0
    def incrementComparisons(self):
        self.numberOfComparisons = self.numberOfComparisons + 1
    def incrementMoves(self):
        self.numberOfMoves = self.numberOfMoves + 1
    def incrementMovesByN(self, n):
        self.numberOfMoves = self.numberOfMoves + n