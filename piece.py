class Piece():
    
    def __init__(self, has_bomb: bool) -> None:
        self.has_bomb = has_bomb
        self.is_clicked = False
        self.is_flagged = False

    def setNeighbors(self, neighbors: list):
        self.neighbors = neighbors
        self.setPieceNumber()

    def setPieceNumber(self):
        self.bomb_number = 0
        for piece in self.neighbors:
            if(piece.getHasBomb()):
                self.bomb_number += 1

    def getPieceNumber(self):
        return self.bomb_number

    def getNeighbors(self):
        return self.neighbors

    def getHasBomb(self):
        return self.has_bomb

    def getIsClicked(self):
        return self.is_clicked

    def getIsFlagged(self):
        return self.is_flagged
    
    def toggleFlag(self):
        self.is_flagged = not self.is_flagged

    def click(self):
        self.is_clicked = True