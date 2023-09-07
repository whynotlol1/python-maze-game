# feel free to use some parts of this code in your project

import __global_data__
import map_generation
import pygame
import math
import time


def main() -> None:
    # initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((__global_data__.GAME["BOUNDS"][0], __global_data__.GAME["BOUNDS"][1]))
    pygame.display.set_caption(f"Maze game v{__global_data__.GAME['VERSION']}")
    clock = pygame.time.Clock()
    # generating the map
    game_surface = map_generation.generate(width=__global_data__.GAME["BOUNDS"][1], height=__global_data__.GAME["BOUNDS"][0], iterations=1)
    # generating entrance and exit points
    # entrance
    game_surface[0][0] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"]][__global_data__.GAME["UNIT_SIZE"]] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"] * 2][__global_data__.GAME["UNIT_SIZE"] * 2] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"]][__global_data__.GAME["UNIT_SIZE"] * 2] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"] * 2][__global_data__.GAME["UNIT_SIZE"]] = 2
    game_surface[0][__global_data__.GAME["UNIT_SIZE"]] = 2
    game_surface[0][__global_data__.GAME["UNIT_SIZE"] * 2] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"]][0] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"] * 2][0] = 2
    # exit
    # TODO

    while __global_data__.GAME["IS_RUNNING"]:
        clock.tick(__global_data__.GAME["FPS_STANDART"])
        # rendering
        # filling the screen black
        screen.fill(__global_data__.COLORS["BLACK"])

        # rendering the maze part seen to the player
        for x_pos in range(0, __global_data__.GAME["BOUNDS"][0], __global_data__.GAME["UNIT_SIZE"]):
            for y_pos in range(0, __global_data__.GAME["BOUNDS"][1], __global_data__.GAME["UNIT_SIZE"]):
                DISTANCE = math.sqrt((x_pos - __global_data__.PLAYER["POSITION"]["X"]) ** 2 + (y_pos - __global_data__.PLAYER["POSITION"]["Y"]) ** 2)
                if DISTANCE <= (
                        __global_data__.PLAYER["VIEW"]["FACTOR"] * __global_data__.PLAYER["VIEW"]["STRENGTH_FACTOR"]):
                    match game_surface[x_pos][y_pos]:
                        case 0:  # floor
                            pygame.draw.rect(screen, __global_data__.COLORS["BLACK"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
                        case 1:  # wall
                            pygame.draw.rect(screen, __global_data__.COLORS["WHITE"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
                        case 2:  # entrance or exit
                            pygame.draw.rect(screen, __global_data__.COLORS["YELLOW"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))

        # rendering the player
        pygame.draw.circle(screen, __global_data__.COLORS["RED"], (__global_data__.PLAYER["POSITION"]["X"], __global_data__.PLAYER["POSITION"]["Y"]), int(__global_data__.GAME["UNIT_SIZE"] / 3))

        pygame.display.update()

        # debug mode
        debug_mode = False

        # controls
        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_w] and __global_data__.PLAYER["POSITION"]["Y"] > 0:  # [W]
            __global_data__.PLAYER["POSITION"]["Y"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_s] and __global_data__.PLAYER["POSITION"]["Y"] < __global_data__.GAME["BOUNDS"][0]:  # [S]
            __global_data__.PLAYER["POSITION"]["Y"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_a] and __global_data__.PLAYER["POSITION"]["X"] > 0:  # [A]
            __global_data__.PLAYER["POSITION"]["X"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_d] and __global_data__.PLAYER["POSITION"]["X"] < __global_data__.GAME["BOUNDS"][1]:  # [D]
            __global_data__.PLAYER["POSITION"]["X"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_x]:  # enable / disable debug mode
            debug_mode = True if not debug_mode else False
            if debug_mode:
                __global_data__.PLAYER["VIEW"]["FACTOR"] = 100
                __global_data__.PLAYER["VIEW"]["STRENGTH_FACTOR"] = 1000
            else:
                __global_data__.PLAYER["VIEW"]["FACTOR"] = 0.4
                __global_data__.PLAYER["VIEW"]["STRENGTH_FACTOR"] = 200
            time.sleep(0.1)

        elif KEYS[pygame.K_ESCAPE]:  # quitting if [ESC] is pressed
            pygame.quit()
            __global_data__.GAME["IS_RUNNING"] = False

        for event in pygame.event.get():  # quitting if X is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                __global_data__.GAME["IS_RUNNING"] = False


if __name__ == "__main__":
    main()
