# Feel free to use some parts of this code in your project

import __global_data__
import map_generation
import pygame

def main():
    # Initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((__global_data__.GAME["BOUNDS"], __global_data__.GAME["BOUNDS"]))
    pygame.display.set_caption(f"Maze game v{__global_data__.GAME['VERSION']}")
    clock = pygame.time.Clock()
    # Generating the map
    game_surface = map_generation.generate(width=__global_data__.GAME["BOUNDS"], height=__global_data__.GAME["BOUNDS"], iterations=1)
    # Drawing the 2 remaining borders (as the originally generated borders are out of reach for the rendering algorithm)
    game_surface[__global_data__.GAME["BOUNDS"] - 1] = [1 for _ in range(__global_data__.GAME["BOUNDS"])]
    # Generating entrance and exit points
    # Entrance
    for i in range(3):
        game_surface[i * __global_data__.GAME["UNIT_SIZE"]][i * __global_data__.GAME["UNIT_SIZE"]] = 2
        game_surface[0][i * __global_data__.GAME["UNIT_SIZE"]] = 2
        game_surface[i * __global_data__.GAME["UNIT_SIZE"]][0] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"]][2 * __global_data__.GAME["UNIT_SIZE"]] = 2
    game_surface[2 * __global_data__.GAME["UNIT_SIZE"]][__global_data__.GAME["UNIT_SIZE"]] = 2
    # Exit
    # TODO

    while __global_data__.GAME["IS_RUNNING"]:
        clock.tick(__global_data__.GAME["FPS_STANDART"])
        # Rendering
        # Filling the screen black
        screen.fill(__global_data__.COLORS["BLACK"])

        # Rendering the maze part seen to the player
        for x_pos in range(0, __global_data__.GAME["BOUNDS"], __global_data__.GAME["UNIT_SIZE"]):
            for y_pos in range(0, __global_data__.GAME["BOUNDS"], __global_data__.GAME["UNIT_SIZE"]):
                match game_surface[x_pos][y_pos]:
                    case 0:  # Floor
                        pygame.draw.rect(screen, __global_data__.COLORS["BLACK"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
                    case 1:  # Wall
                        pygame.draw.rect(screen, __global_data__.COLORS["WHITE"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
                    case 2:  # Entrance or exit
                        pygame.draw.rect(screen, __global_data__.COLORS["YELLOW"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))

        # Rendering the player
        pygame.draw.circle(screen, __global_data__.COLORS["RED"], (__global_data__.PLAYER["POSITION"]["X"], __global_data__.PLAYER["POSITION"]["Y"]), int(__global_data__.GAME["UNIT_SIZE"] / 3))

        pygame.display.update()

        # Controls
        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_w] and __global_data__.PLAYER["POSITION"]["Y"] > 0:  # [W]
            __global_data__.PLAYER["POSITION"]["Y"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_s] and __global_data__.PLAYER["POSITION"]["Y"] < __global_data__.GAME["BOUNDS"]:  # [S]
            __global_data__.PLAYER["POSITION"]["Y"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_a] and __global_data__.PLAYER["POSITION"]["X"] > 0:  # [A]
            __global_data__.PLAYER["POSITION"]["X"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_d] and __global_data__.PLAYER["POSITION"]["X"] < __global_data__.GAME["BOUNDS"]:  # [D]
            __global_data__.PLAYER["POSITION"]["X"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_ESCAPE]:  # Quitting if [ESC] is pressed
            pygame.quit()
            __global_data__.GAME["IS_RUNNING"] = False

        for event in pygame.event.get():  # Quitting if X is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                __global_data__.GAME["IS_RUNNING"] = False


if __name__ == "__main__":
    main()
