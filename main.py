# Feel free to use some parts of this code in your project

from map_generation import game_surface
from __game_initialization__ import *
import __global_data__
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
    # Variable for rendering the congratulation text
    render_congratulation = False

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
        if __global_data__.PLAYER["IS_RENDERED"]:
            pygame.draw.circle(screen, __global_data__.COLORS["RED"], (__global_data__.PLAYER["POSITION"]["X"] + __global_data__.GAME["UNIT_SIZE"] / 2, __global_data__.PLAYER["POSITION"]["Y"] + __global_data__.GAME["UNIT_SIZE"] / 2), int(__global_data__.GAME["UNIT_SIZE"] / 3))

        # Controls
        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_w] and __global_data__.PLAYER["POSITION"]["Y"] > 0:  # [W]
            new_x = __global_data__.PLAYER["POSITION"]["X"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"] - __global_data__.PLAYER["SPEED"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    __global_data__.PLAYER["IS_RENDERED"] = False
                    render_congratulation = True
                else:
                    __global_data__.PLAYER["POSITION"]["Y"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_s] and __global_data__.PLAYER["POSITION"]["Y"] < __global_data__.GAME["BOUNDS"]:  # [S]
            new_x = __global_data__.PLAYER["POSITION"]["X"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"] + __global_data__.PLAYER["SPEED"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    __global_data__.PLAYER["IS_RENDERED"] = False
                    render_congratulation = True
                else:
                    __global_data__.PLAYER["POSITION"]["Y"] += __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_a] and __global_data__.PLAYER["POSITION"]["X"] > 0:  # [A]
            new_x = __global_data__.PLAYER["POSITION"]["X"] - __global_data__.PLAYER["SPEED"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    __global_data__.PLAYER["IS_RENDERED"] = False
                    render_congratulation = True
                else:
                    __global_data__.PLAYER["POSITION"]["X"] -= __global_data__.PLAYER["SPEED"]

        elif KEYS[pygame.K_d] and __global_data__.PLAYER["POSITION"]["X"] < __global_data__.GAME["BOUNDS"]:  # [D]
            new_x = __global_data__.PLAYER["POSITION"]["X"] + __global_data__.PLAYER["SPEED"]
            new_y = __global_data__.PLAYER["POSITION"]["Y"]
            if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                    __global_data__.PLAYER["IS_RENDERED"] = False
                    render_congratulation = True
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
        except pygame.error:  # Basically not printing out an error after you win
            pass

        # Rendering the congratulation text
        if render_congratulation:
            screen.fill(__global_data__.COLORS["BLACK"])
            text = my_font.render("Congratulations on beating the maze!", False, __global_data__.COLORS["WHITE"])
            x_pos = __global_data__.GAME["UNIT_SIZE"]
            y_pos = ((__global_data__.GAME["BOUNDS"] / __global_data__.GAME["UNIT_SIZE"]) / 2) * __global_data__.GAME["UNIT_SIZE"]
            screen.blit(text, (x_pos, y_pos))

        # Screen updates
        pygame.display.update()


if __name__ == "__main__":
    main()
