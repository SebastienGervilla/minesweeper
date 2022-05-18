from piece import Piece
from board import Board
import pygame
import os
from time import sleep

class Game():

    def __init__(self, board: Board, screen_size: tuple, game_size: tuple):
        self.board = board
        self.screen_size = screen_size
        self.game_size = game_size
        self.piece_size = self.game_size[0] // self.board.getSize()[1], self.game_size[1] // self.board.getSize()[0]
        self.start_pos = self.getStartPos()
        self.loadImages()

    def getStartPos(self):
        left_pos = (self.screen_size[0] - self.game_size[0]) // 2
        top_pos = self.screen_size[1] - 11 * self.game_size[1] // 10
        return (left_pos, top_pos)

    def isRunning(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill((255,255,255))
        is_running = True
        while(is_running):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    is_running = False
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    mouse_pos = pygame.mouse.get_pos()
                    isRightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(mouse_pos, isRightClick)
            self.draw()
            pygame.display.flip()
            if (self.board.getWon()):
                sleep(3)
                is_running = False
        pygame.quit()

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("assets/MineSweeper"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"assets/MineSweeper/" + fileName)
            image = pygame.transform.scale(image, self.piece_size)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece: Piece):
        file_name = None
        if (piece.getIsClicked()):
            if (piece.getHasBomb()):
                file_name = "clicked-bomb"
            else:
                file_name = "minesweeper_" + str(piece.getPieceNumber())
        else:
            if(piece.getIsFlagged()):
                file_name = "unclicked-flag"
            else:
                file_name = "unclicked-square"
        # else:
        #     image_name = "minesweeper_" + str(piece.getPieceNumber())

        return self.images[file_name]

    def handleClick(self, mouse_pos: tuple, isRightClick: bool):
        if (self.board.getLost()):
            return
        if (self.game_size[0] + self.start_pos[0] > mouse_pos[0] > self.start_pos[0]  # If in the game screen
        or self.game_size[1] + self.start_pos[1] > mouse_pos[1] > self.start_pos[1]):
            index = ((mouse_pos[1] - self.start_pos[1]) // self.piece_size[1],
            (mouse_pos[0] - self.start_pos[0]) // self.piece_size[0])
            index = (int(index[0]) , int(index[1]))
            self.board.handleClick(self.board.getPiece(index[0], index[1]), isRightClick)


    def draw(self):
        piece_pos = self.start_pos
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece(row, col)
                image = self.getImage(piece)
                self.screen.blit(image, piece_pos)
                piece_pos = piece_pos[0] + self.piece_size[0], piece_pos[1]
            piece_pos = self.start_pos[0], piece_pos[1] + self.piece_size[1]