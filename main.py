from game import Game
from board import Board

WIDTH, HEIGHT = 800, 800
ROW, COL = 10, 10
WHITE = (255, 255, 255)
FPS = 60

def main():
    bomb_prob = 0.1
    screen_size = (WIDTH, HEIGHT)
    game_size = (2 * WIDTH / 3, 2 * HEIGHT / 3)
    board = Board((ROW, COL), bomb_prob)
    game = Game(board, screen_size, game_size)
    game.isRunning()

if __name__ == "__main__":
    main()