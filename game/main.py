# Feel free to use some parts of this code in your project

from game.__global__.__game_initialisation__ import *
from game.__global__.__global_data__ import *
import map_generation
import pygame


def collision_handler(game_map: list[list[int]], x_pos: int, y_pos: int, checking_code: str) -> bool or str:
    try:
        match checking_code:
            case "wall":
                # Checking if the given point (x, y) is not a wall. Returning True if you cannot move there.
                return game_map[x_pos][y_pos] == 1
            case "exit":
                # Checking if the given point (x, y) is an exit. Returning True if it's an exit
                return game_map[x_pos][y_pos] == 3
    except IndexError:  # Still returning a collision even if the index is somehow out of range
        return True
    # Returning an exception if something goes wrong
    return "CollisionHandlerException: Unknown error occurred"


game_surface = map_generation.generate_level()


def main():
    global game_surface
    saved_game_speed = GAME["GAME_SPEED"]

    def restart():
        global game_surface
        game_surface = map_generation.generate_level()
        PLAYER["POSITION"][0] = GAME["UNIT_SIZE"]
        PLAYER["POSITION"][1] = GAME["UNIT_SIZE"]
        GAME["LEVEL"] = "LEVEL-1"

    while GAME["IS_RUNNING"]:
        clock.tick(GAME["GAME_SPEED"])
        # Rendering
        # Filling the screen black
        screen.fill(COLORS["BLACK"])

        # Main menu or level rendering
        match GAME["LEVEL"]:
            case "MAIN-MENU":
                GAME["GAME_SPEED"] = 120
                # Rendering the cursor
                mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, COLORS["RED"], (mouse[0] + GAME["UNIT_SIZE"] / 2, mouse[1] + GAME["UNIT_SIZE"] / 2), GAME["UNIT_SIZE"] / 3)
                # Rendering the buttons
                text = my_font.render(f"Welcome to {name}", False, COLORS["WHITE"])
                screen.blit(text, (GAME["BOUNDS"] / 14, 100))
                for button in buttons:
                    if GAME["LEVEL"] in buttons[button]["IS_RENDERED_ON"]:
                        pygame.draw.rect(screen, COLORS["WHITE"], (buttons[button]["POSITION"][0], buttons[button]["POSITION"][1], button_width, button_height), 5)
                        text = my_font.render(buttons[button]["TEXT"], False, COLORS["WHITE"])
                        x_pos = buttons[button]["POSITION"][0] + 5
                        y_pos = buttons[button]["POSITION"][1] + 5
                        screen.blit(text, (x_pos, y_pos))

            case "LEVEL-1":
                GAME["GAME_SPEED"] = saved_game_speed
                # Rendering the maze part seen to the player
                for x_pos in range(0, GAME["BOUNDS"], GAME["UNIT_SIZE"]):
                    for y_pos in range(0, GAME["BOUNDS"], GAME["UNIT_SIZE"]):
                        match game_surface[x_pos][y_pos]:
                            case 0:  # Floor
                                pygame.draw.rect(screen, COLORS["BLACK"], (x_pos, y_pos, x_pos + GAME["UNIT_SIZE"], y_pos + GAME["UNIT_SIZE"]))
                            case 1:  # Wall
                                pygame.draw.rect(screen, COLORS["WHITE"], (x_pos, y_pos, x_pos + GAME["UNIT_SIZE"], y_pos + GAME["UNIT_SIZE"]))
                            case 2:  # Entrance
                                pygame.draw.rect(screen, COLORS["YELLOW"], (x_pos, y_pos, x_pos + GAME["UNIT_SIZE"], y_pos + GAME["UNIT_SIZE"]))
                            case 3:
                                pygame.draw.rect(screen, COLORS["YELLOW"], (x_pos, y_pos, x_pos + GAME["UNIT_SIZE"], y_pos + GAME["UNIT_SIZE"]))

                # Rendering the player
                pygame.draw.circle(screen, COLORS["RED"], (PLAYER["POSITION"]["X"] + GAME["UNIT_SIZE"] / 2, PLAYER["POSITION"]["Y"] + GAME["UNIT_SIZE"] / 2), int(GAME["UNIT_SIZE"] / 3))

                # Controls
                KEYS = pygame.key.get_pressed()

                if KEYS[pygame.K_w] and PLAYER["POSITION"]["Y"] > 0:  # [W]
                    new_x = PLAYER["POSITION"]["X"]
                    new_y = PLAYER["POSITION"]["Y"] - PLAYER["SPEED"]
                    if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                        if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                            GAME["LEVEL"] = "CONGRATULATION"
                        else:
                            PLAYER["POSITION"]["Y"] -= PLAYER["SPEED"]

                elif KEYS[pygame.K_s] and PLAYER["POSITION"]["Y"] < GAME["BOUNDS"]:  # [S]
                    new_x = PLAYER["POSITION"]["X"]
                    new_y = PLAYER["POSITION"]["Y"] + PLAYER["SPEED"]
                    if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                        if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                            GAME["LEVEL"] = "CONGRATULATION"
                        else:
                            PLAYER["POSITION"]["Y"] += PLAYER["SPEED"]

                elif KEYS[pygame.K_a] and PLAYER["POSITION"]["X"] > 0:  # [A]
                    new_x = PLAYER["POSITION"]["X"] - PLAYER["SPEED"]
                    new_y = PLAYER["POSITION"]["Y"]
                    if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                        if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                            GAME["LEVEL"] = "CONGRATULATION"
                        else:
                            PLAYER["POSITION"]["X"] -= PLAYER["SPEED"]

                elif KEYS[pygame.K_d] and PLAYER["POSITION"]["X"] < GAME["BOUNDS"]:  # [D]
                    new_x = PLAYER["POSITION"]["X"] + PLAYER["SPEED"]
                    new_y = PLAYER["POSITION"]["Y"]
                    if not collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="wall"):
                        if collision_handler(game_map=game_surface, x_pos=new_x, y_pos=new_y, checking_code="exit"):
                            GAME["LEVEL"] = "CONGRATULATION"
                        else:
                            PLAYER["POSITION"]["X"] += PLAYER["SPEED"]

            case "CONGRATULATION":
                # Rendering the congratulation text
                screen.fill(COLORS["BLACK"])
                text = my_font.render("Congratulations on beating the maze!", False, COLORS["WHITE"])
                x_pos = GAME["BOUNDS"] / 16
                y_pos = ((GAME["BOUNDS"] / GAME["UNIT_SIZE"]) / 4) * GAME["UNIT_SIZE"]
                screen.blit(text, (x_pos, y_pos))
                # Rendering the cursor
                mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, COLORS["RED"], (mouse[0] + GAME["UNIT_SIZE"] / 2, mouse[1] + GAME["UNIT_SIZE"] / 2), GAME["UNIT_SIZE"] / 3)
                # Rendering the buttons
                for button in buttons:
                    if GAME["LEVEL"] in buttons[button]["IS_RENDERED_ON"]:
                        pygame.draw.rect(screen, COLORS["WHITE"], (buttons[button]["POSITION"][0], buttons[button]["POSITION"][1], button_width, button_height), 5)
                        text = my_font.render(buttons[button]["TEXT"], False, COLORS["WHITE"])
                        x_pos = buttons[button]["POSITION"][0] + 5
                        y_pos = buttons[button]["POSITION"][1] + 5
                        screen.blit(text, (x_pos, y_pos))

        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quitting if X is pressed
                    pygame.quit()
                    GAME["IS_RUNNING"] = False
                # Buttons
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAME["LEVEL"] in ["MAIN-MENU", "CONGRATULATION"]:
                        for button in buttons:
                            mouse = pygame.mouse.get_pos()
                            if buttons[button]["POSITION"][0] <= mouse[0] <= buttons[button]["POSITION"][0] + button_width and buttons[button]["POSITION"][1] <= mouse[1] <= buttons[button]["POSITION"][1] + button_height:
                                match buttons[button]["ACTION_CODE"]:
                                    case "QUIT":
                                        pygame.quit()
                                    case "PLAY":
                                        restart()
                                    case "NEW_MAZE":
                                        restart()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Quitting if [ESC] is pressed
                pygame.quit()
                GAME["IS_RUNNING"] = False
            elif pygame.key.get_pressed()[pygame.K_EQUALS]:  # If you`re trapped
                GAME["LEVEL"] = "MAIN-MENU"

            # Screen updates
            pygame.display.update()

        except pygame.error:  # Basically quitting the game correctly
            exit(0)


if __name__ == "__main__":
    main()
