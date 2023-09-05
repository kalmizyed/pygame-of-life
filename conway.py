import pygame
import board
import rules

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
TILE_SIZE = 1
GAME_TICK = 20
GAME_RULE = rules.CONWAY
SEED_FRAC = 2

def render():
    screen.fill(0)
    state = gameBoard.board
    pixels = pygame.PixelArray(screen)
    for row in range(SCREEN_HEIGHT):
        for col in range(SCREEN_WIDTH):
            boardPos = gameBoard.asBoardPos((col, row))
            pixels[col, row] = int(state[boardPos]) * 0xAAAAAA
    pixels.close()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)
running = True
paused = True
clicking = False
gameBoard = board.Board(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, GAME_RULE, SEED_FRAC)

render()
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = True if paused == False else False
            if event.key == pygame.K_RETURN:
                gameBoard.initialize()
            if event.key == pygame.K_BACKSPACE:
                gameBoard.clear()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = False
            gameBoard.clearMouseHistory()
    
    if clicking:
        gameBoard.handleMouse(pygame.mouse.get_pos())
        render()
    
    clock.tick(GAME_TICK)
    if paused == False:
        gameBoard.update()
        render()

    pygame.display.flip()
    
pygame.quit()