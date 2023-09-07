# Feel free to use some parts of this code in your project

import __global_data__
import map_generation
import random
import pygame


def collision_handler(game_map: list[list[int]], x_pos: int, y_pos: int, checking_code: str) -> bool or str:
    match checking_code:
        case "wall":
            # Checking if the given point (x, y) is not a wall. Returns True if you cannot move there.
            try:
                return game_map[x_pos][y_pos] == 1
            except IndexError:  # Still returning a collision even if the index is somehow out of range
                return True
        case "exit":
            # Checking if the given point (x, y) is an exit. Returns True if it's an exit
            try:
                return game_map[x_pos][y_pos] == 3
            except IndexError:  # Still returning a collision even if the index is somehow out of range
                return True
    # Returning an exception if something goes wrong
    return "CollisionHandlerException: Unknown error occurred"


def main():
    # Initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((__global_data__.GAME["BOUNDS"], __global_data__.GAME["BOUNDS"]))
    pygame.display.set_caption(f"Maze game v{__global_data__.GAME['VERSION']}")
    clock = pygame.time.Clock()
    # Generating the map
    game_surface = map_generation.generate(width=__global_data__.GAME["BOUNDS"], height=__global_data__.GAME["BOUNDS"], iterations=1)
    # Drawing the 2 remaining borders (as the originally generated borders are out of reach for the rendering algorithm)
    # Bottom border
    game_surface[__global_data__.GAME["BOUNDS"] - __global_data__.GAME["UNIT_SIZE"]] = [1 for _ in range(__global_data__.GAME["BOUNDS"])]
    # Right border
    for i in range(0, __global_data__.GAME["BOUNDS"], __global_data__.GAME["UNIT_SIZE"]):
        game_surface[i][__global_data__.GAME["BOUNDS"] - __global_data__.GAME["UNIT_SIZE"]] = 1
    # Generating entrance and exit points
    # Entrance
    for i in range(3):
        game_surface[i * __global_data__.GAME["UNIT_SIZE"]][i * __global_data__.GAME["UNIT_SIZE"]] = 2
        game_surface[0][i * __global_data__.GAME["UNIT_SIZE"]] = 2
        game_surface[i * __global_data__.GAME["UNIT_SIZE"]][0] = 2
    game_surface[__global_data__.GAME["UNIT_SIZE"]][2 * __global_data__.GAME["UNIT_SIZE"]] = 2
    game_surface[2 * __global_data__.GAME["UNIT_SIZE"]][__global_data__.GAME["UNIT_SIZE"]] = 2
    # Exit
    exit_side = random.choice(["right", "bottom"])  # Choosing the side for the exit to generate on
    match exit_side:
        case "bottom":
            # Bottom border
            exit_y = __global_data__.GAME["BOUNDS"] - __global_data__.GAME["UNIT_SIZE"]
            # Inbetween the middle of the border and the corner
            exit_x = random.randint(int((__global_data__.GAME["BOUNDS"] / __global_data__.GAME["UNIT_SIZE"] / 2)), int(__global_data__.GAME["BOUNDS"] / __global_data__.GAME["UNIT_SIZE"]) - 1)
            game_surface[exit_x * __global_data__.GAME["UNIT_SIZE"] + __global_data__.GAME["UNIT_SIZE"]][exit_y] = 3
            game_surface[exit_x * __global_data__.GAME["UNIT_SIZE"]][exit_y] = 3
            game_surface[exit_x * __global_data__.GAME["UNIT_SIZE"] - __global_data__.GAME["UNIT_SIZE"]][exit_y] = 3
        case "right":
            # Right border
            exit_x = __global_data__.GAME["BOUNDS"] - __global_data__.GAME["UNIT_SIZE"]
            # Inbetween the middle of the border and the corner
            exit_y = random.randint(int((__global_data__.GAME["BOUNDS"] / __global_data__.GAME["UNIT_SIZE"] / 2)), int(__global_data__.GAME["BOUNDS"] / __global_data__.GAME["UNIT_SIZE"]) - 1)
            game_surface[exit_x][exit_y * __global_data__.GAME["UNIT_SIZE"] + __global_data__.GAME["UNIT_SIZE"]] = 3
            game_surface[exit_x][exit_y * __global_data__.GAME["UNIT_SIZE"]] = 3
            game_surface[exit_x][exit_y * __global_data__.GAME["UNIT_SIZE"] - __global_data__.GAME["UNIT_SIZE"]] = 3

    while __global_data__.GAME["IS_RUNNING"]:
        clock.tick(__global_data__.GAME["GAME_SPEED"])
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
                    case 2:  # Entrance
                        pygame.draw.rect(screen, __global_data__.COLORS["YELLOW"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
                    case 3:
                        pygame.draw.rect(screen, __global_data__.COLORS["YELLOW"], (x_pos, y_pos, x_pos + __global_data__.GAME["UNIT_SIZE"], y_pos + __global_data__.GAME["UNIT_SIZE"]))
        # Rendering the player
        pygame.draw.circle(screen, __global_data__.COLORS["RED"], (__global_data__.PLAYER["POSITION"]["X"] + __global_data__.GAME["UNIT_SIZE"] / 2, __global_data__.PLAYER["POSITION"]["Y"] + __global_data__.GAME["UNIT_SIZE"] / 2), int(__global_data__.GAME["UNIT_SIZE"] / 3))

        pygame.display.update()

        # Controls
        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_w] and __global_data__.PLAYER["POSITION"]["Y"] > 0:  # [W]
            new_x = __global_data__.PLAYER["POSITION"]["X"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"] - __global_data__.PLAYER["SPEED"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    print("=" * 100)
                    print("You've successfully beaten the maze. A proper congratulation will be added soon.")
                    print("=" * 100)
                    pygame.quit()
                    __global_data__.GAME["IS_RUNNING"] = False
                else:
                    __global_data__.PLAYER["POSITION"]["Y"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_s] and __global_data__.PLAYER["POSITION"]["Y"] < __global_data__.GAME["BOUNDS"]:  # [S]
            new_x = __global_data__.PLAYER["POSITION"]["X"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"] + __global_data__.PLAYER["SPEED"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    print("=" * 100)
                    print("You've successfully beaten the maze. A proper congratulation will be added soon.")
                    print("=" * 100)
                    pygame.quit()
                    __global_data__.GAME["IS_RUNNING"] = False
                else:
                    __global_data__.PLAYER["POSITION"]["Y"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_a] and __global_data__.PLAYER["POSITION"]["X"] > 0:  # [A]
            new_x = __global_data__.PLAYER["POSITION"]["X"] - __global_data__.PLAYER["SPEED"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    print("=" * 100)
                    print("You've successfully beaten the maze. A proper congratulation will be added soon.")
                    print("=" * 100)
                    pygame.quit()
                    __global_data__.GAME["IS_RUNNING"] = False
                else:
                    __global_data__.PLAYER["POSITION"]["X"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_d] and __global_data__.PLAYER["POSITION"]["X"] < __global_data__.GAME["BOUNDS"]:  # [D]
            new_x = __global_data__.PLAYER["POSITION"]["X"] + __global_data__.PLAYER["SPEED"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    print("=" * 100)
                    print("You've successfully beaten the maze. A proper congratulation will be added soon.")
                    print("=" * 100)
                    pygame.quit()
                    __global_data__.GAME["IS_RUNNING"] = False
                else:
                    __global_data__.PLAYER["POSITION"]["X"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_ESCAPE]:  # Quitting if [ESC] is pressed
            pygame.quit()
            __global_data__.GAME["IS_RUNNING"] = False
        try:
            for event in pygame.event.get():  # Quitting if X is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    __global_data__.GAME["IS_RUNNING"] = False
        except pygame.error:
            pass


if __name__ == "__main__":
    main()
