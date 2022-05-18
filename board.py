from piece import Piece
import random


class Board():

    def __init__(self, board_size: tuple, bomb_prob: float) -> None:
        self.board_size = board_size
        self.bomb_prob = bomb_prob
        self.has_lost = False
        self.clicked_num = 0
        self.non_bomb_num = 0
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range(self.board_size[0]):
            row = []
            for col in range(self.board_size[1]):
                has_bomb = random.random() < self.bomb_prob # Random gives a float in the range [0.0, 1.0), so prob needs same range
                if (not has_bomb):
                    self.non_bomb_num += 1
                piece = Piece(has_bomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors(piece)

    def setNeighbors(self, piece: Piece):
        for row in range(self.board_size[0]):
            for col in range(self.board_size[1]):
                piece = self.getPiece(row, col)
                neighbors = self.getNeighborsList((row, col))
                piece.setNeighbors(neighbors)

    def getNeighborsList(self, index: tuple):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                out_of_bounds = False
                same = False
                if(row < 0 or row >= self.board_size[0] or col < 0 or col >= self.board_size[1]):
                    out_of_bounds = True
                if(row == index[0] and col == index[1]):
                    same = True

                if(same or out_of_bounds):
                    continue
                neighbors.append(self.getPiece(row, col))
        return neighbors

    def getPiece(self, row: int, col: int):
        return self.board[row][col]

    def getSize(self):
        return self.board_size

    def handleClick(self, piece: Piece, isRightClick: bool):
        if(piece.getIsClicked() or (not isRightClick and piece.getIsFlagged())):
            return
        if(isRightClick):
            piece.toggleFlag()
            return
        piece.click()
        if (piece.getHasBomb()):
            self.has_lost = True
            return
        self.clicked_num += 1
        if (piece.getPieceNumber() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getIsClicked()):
                self.handleClick(neighbor, False)

    def getLost(self):
        return self.has_lost

    def getWon(self):
        return self.non_bomb_num == self.clicked_num