import pygame

# Constants
WIDTH = 640
HEIGHT = 480
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 80
RADIUS = int(SQUARE_SIZE / 2 - 5)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Four in a Row")

# Create the game board
board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]


def draw_board():
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + int(SQUARE_SIZE / 2),
                                               (row + 1) * SQUARE_SIZE + int(SQUARE_SIZE / 2)), RADIUS)

    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + int(SQUARE_SIZE / 2),
                                                 (row + 1) * SQUARE_SIZE + int(SQUARE_SIZE / 2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + int(SQUARE_SIZE / 2),
                                                    (row + 1) * SQUARE_SIZE + int(SQUARE_SIZE / 2)), RADIUS)

    pygame.display.update()


def drop_piece(row, col, piece):
    board[row][col] = piece


def is_valid_location(col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def winning_move(piece):
    # Check horizontal locations for win
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and \
                    board[row][col + 3] == piece:
                return True

    # Check vertical locations for win
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and \
                    board[row + 3][col] == piece:
                return True

    # Check positively sloped diagonals
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and \
                    board[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for row in range(ROW_COUNT - 3):
        for col in range(3, COLUMN_COUNT):
            if board[row][col] == piece and board[row + 1][col - 1] == piece and board[row + 2][col - 2] == piece and \
                    board[row + 3][col - 3] == piece:
                return True

    return False


# Game loop
turn = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get column from player's input
            if turn % 2 == 0:
                col = event.pos[0] // SQUARE_SIZE
                if is_valid_location(col):
                    row = get_next_open_row(col)
                    drop_piece(row, col, 1)
                    if winning_move(1):
                        print("Player 1 wins!")
                        game_over = True
            else:
                col = event.pos[0] // SQUARE_SIZE
                if is_valid_location(col):
                    row = get_next_open_row(col)
                    drop_piece(row, col, 2)
                    if winning_move(2):
                        print("Player 2 wins!")
                        game_over = True
            draw_board()
            turn += 1

pygame.quit()
