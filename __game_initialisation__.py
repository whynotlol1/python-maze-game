import __global_data__
import pygame

# Initialising pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Roboto', 50)
screen = pygame.display.set_mode((__global_data__.GAME["BOUNDS"], __global_data__.GAME["BOUNDS"]))
pygame.display.set_caption(f"Maze game v{__global_data__.GAME['VERSION']}")
clock = pygame.time.Clock()
