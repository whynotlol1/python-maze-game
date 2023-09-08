import __global_data__
import pygame

# Initialising pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Roboto', 50)
screen = pygame.display.set_mode((__global_data__.GAME["BOUNDS"], __global_data__.GAME["BOUNDS"]))
name = f"Maze game v{__global_data__.GAME['VERSION']}"
pygame.display.set_caption(name)
clock = pygame.time.Clock()

# Initialising buttons
button_width = 100
button_height = 50
buttons = {
    "QUIT": {
        "TEXT": "Quit",
        "ACTION_CODE": "QUIT",
        "POSITION": [__global_data__.GAME["BOUNDS"] / 6, 300],
        "IS_RENDERED_ON": ["MAIN-MENU", "CONGRATULATION"]
    },
    "PLAY": {
        "TEXT": "Play",
        "ACTION_CODE": "PLAY",
        "POSITION": [(__global_data__.GAME["BOUNDS"] / 6) * 4, 300],
        "IS_RENDERED_ON": ["MAIN-MENU"]
    },
    "NEW_MAZE": {
        "TEXT": "Try again",
        "ACTION_CODE": "RETRY",
        "POSITION": [(__global_data__.GAME["BOUNDS"] / 6) * 4, 300],
        "IS_RENDERED_ON": ["CONGRATULATION"]
    }
}
